<?php
include 'api.php';
$apiUrl = 'http://localhost:5000/products';

// Handle POST (Create)
if (isset($_POST['action']) && $_POST['action'] === 'create') {
    $data = [
        'name' => $_POST['name'],
        'description' => $_POST['description'],
        'price' => (float)$_POST['price'],
        'energy_type' => $_POST['energy_type']
    ];
    api_request($apiUrl, 'POST', $data);
    header("Location: index.php");
}

// Handle PUT (Update)
if (isset($_POST['action']) && $_POST['action'] === 'update') {
    $id = $_POST['id'];
    $data = [
        'name' => $_POST['name'],
        'description' => $_POST['description'],
        'price' => (float)$_POST['price'],
        'energy_type' => $_POST['energy_type']
    ];
    api_request("$apiUrl/$id", 'PUT', $data);
    header("Location: index.php");
}

// Handle DELETE
if (isset($_GET['delete'])) {
    $id = $_GET['delete'];
    api_request("$apiUrl/$id", 'DELETE');
    header("Location: index.php");
}

$products = api_request($apiUrl);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rekomendasi Produk Energi Terbarukan</title>

    <!-- Tailwind CSS via CDN -->
    <script src="https://cdn.tailwindcss.com"></script>

        <!-- Custom Tailwind Config -->
        <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: {
                            light: '#60a5fa',
                            DEFAULT: '#3b82f6',
                            dark: '#2563eb',
                        },
                    },
                    animation: {
                        'bounce-slow': 'bounce 3s infinite',
                    }
                }
            }
        }
    </script>


</head>
<body class="bg-gray-200 p-6 text-lg">
    <h1 class="text-2xl font-bold mb-4 text-center text-primary animate-bounce-slow">Rekomendasi Produk Energi Terbarukan</h1>


    <!-- Form Tambah -->
    <div class="bg-white p-6 rounded shadow mb-6 max-w-xl mx-auto">
        <h2 class="text-xl font-semibold mb-4">Tambah Produk</h2>
        <form method="post" class="space-y-4">
            <input type="hidden" name="action" value="create">

            <div>
                <label class="block mb-1 font-medium">Nama Produk</label>
                <input name="name" placeholder="Nama Produk" required class="border p-2 rounded w-full">
            </div>

            <div>
                <label class="block mb-1 font-medium">Harga</label>
                <input name="price" placeholder="Harga (Rp)" required type="number" step="0.01" class="border p-2 rounded w-full">
            </div>

            <div>
                <label class="block mb-1 font-medium">Tipe Energi</label>
                <select name="energy_type" required class="border p-2 rounded w-full">
                    <option value="">Pilih Tipe Energi</option>
                    <option value="Surya">Surya</option>
                    <option value="Angin">Angin</option>
                    <option value="Air">Air</option>
                    <option value="Biomassa">Biomassa</option>
                    <option value="Panas Bumi">Panas Bumi</option>
                </select>
            </div>

            <div>
                <label class="block mb-1 font-medium">Deskripsi</label>
                <textarea name="description" placeholder="Deskripsi Produk" class="border p-2 rounded w-full" rows="4"></textarea>
            </div>

            <button class="bg-primary hover:bg-primary-dark text-white px-4 py-2 rounded transition-all">
                Tambahkan Produk
            </button>
        </

    <!-- Tabel Data -->
    <table class="min-w-full bg-white rounded shadow">
        <thead class="bg-gray-200">
            <tr>
                <th class="p-2 text-left">ID</th>
                <th class="p-2 text-left">Nama</th>
                <th class="p-2 text-left">Harga</th>
                <th class="p-2 text-left">Energi</th>
                <th class="p-2 text-left">Aksi</th>
            </tr>
        </thead>
        <tbody>
        <?php foreach ($products as $p): ?>
            <tr class="border-b">
                <td class="p-2"><?= $p['id'] ?></td>
                <td class="p-2"><?= $p['name'] ?></td>
                <td class="p-2">Rp <?= $p['price'] ?></td>
                <td class="p-2"><?= $p['energy_type'] ?></td>
                <td class="p-2">
                    <form method="post" class="inline-block">
                        <input type="hidden" name="action" value="update">
                        <input type="hidden" name="id" value="<?= $p['id'] ?>">
                        <input name="name" value="<?= $p['name'] ?>" class="border px-2 py-1 w-24 rounded mb-1 text-sm">
                        <input name="price" value="<?= $p['price'] ?>" class="border px-2 py-1 w-20 rounded mb-1 text-sm">
                        <select name="energy_type" class="border px-2 py-1 w-24 rounded mb-1 text-sm">
                            <option value="Surya" <?= $p['energy_type'] == 'Surya' ? 'selected' : '' ?>>Surya</option>
                            <option value="Angin" <?= $p['energy_type'] == 'Angin' ? 'selected' : '' ?>>Angin</option>
                            <option value="Air" <?= $p['energy_type'] == 'Air' ? 'selected' : '' ?>>Air</option>
                            <option value="Biomassa" <?= $p['energy_type'] == 'Biomassa' ? 'selected' : '' ?>>Biomassa</option>
                            <option value="Panas Bumi" <?= $p['energy_type'] == 'Panas Bumi' ? 'selected' : '' ?>>Panas Bumi</option>
                        </select>
                        <input type="hidden" name="description" value="<?= $p['description'] ?>">
                        <button class="bg-yellow-500 hover:bg-yellow-600 text-white px-2 py-1 rounded text-sm transition-all">Edit</button>

                    </form>
                    <a href="?delete=<?= $p['id'] ?>" class="bg-red-500 hover:bg-red-600 text-white px-2 py-1 rounded text-sm ml-2 transition-all" onclick="return confirm('Yakin ingin hapus?')">Hapus</a>
                </td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>