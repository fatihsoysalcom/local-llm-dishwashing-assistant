import json

def get_dish_recommendation(dish_count):
    """Simulates a local LLM's decision-making for dishwashing.

    This function takes the number of dishes and provides a recommendation
    based on a simple heuristic, mimicking a simplified LLM's logic.
    """
    if dish_count == 0:
        return "Tavalar tertemiz! Yıkamaya gerek yok."
    elif dish_count < 3:
        return f"Sadece {dish_count} tava mı var? Hemen yıkayıp bitirelim!"
    elif dish_count < 7:
        return f"{dish_count} tava birikti. Şimdi yıkamak en iyisi, yoksa daha çok birikir."
    else:
        return f"Vay canına, {dish_count} tava! Belki biraz bekleyebilirsin ama sonra hepsini birden hallet."

def main():
    print("--- Yerel LLM Bulaşık Asistanı ---")
    print("Bu basit asistan, tavalarınızın sayısına göre size önerilerde bulunur.")

    try:
        num_dishes_str = input("Bugün kaç tane tava kullandınız? (Sayı girin): ")
        num_dishes = int(num_dishes_str)

        recommendation = get_dish_recommendation(num_dishes)
        print(f"\nLLM Önerisi: {recommendation}")

    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
