import os
import shutil
import random

# Definir caminhos
orig_dir = "data/archive/Images"
train_dir = "data/train"
test_dir = "data/test"
split_ratio = 0.8  # 80% treino, 20% teste

# Criar diretórios de treino e teste se não existirem
for category in os.listdir(orig_dir):
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(test_dir, category), exist_ok=True)

# Separar imagens
for category in os.listdir(orig_dir):
    category_path = os.path.join(orig_dir, category)
    images = os.listdir(category_path)
    random.shuffle(images)  # Embaralha para garantir distribuição aleatória

    split_idx = int(len(images) * split_ratio)
    train_images = images[:split_idx]
    test_images = images[split_idx:]

    # Mover arquivos
    for img in train_images:
        shutil.move(os.path.join(category_path, img), os.path.join(train_dir, category, img))
    
    for img in test_images:
        shutil.move(os.path.join(category_path, img), os.path.join(test_dir, category, img))

print("Divisão concluída! 🚀")