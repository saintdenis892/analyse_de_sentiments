object Calcul {
  // Fonction pour additionner deux nombres
  def addition(a: Int, b: Int): Int = {
    a + b
  }

  // Fonction pour soustraire deux nombres
  def soustraction(a: Int, b: Int): Int = {
    a - b
  }

  // Fonction pour multiplier deux nombres
  def multiplication(a: Int, b: Int): Int = {
    a * b
  }

  // Fonction pour diviser deux nombres (avec gestion de la division par zéro)
  def division(a: Int, b: Int): Option[Double] = {
    if (b != 0) Some(a.toDouble / b) else None
  }

  // Fonction principale pour tester les opérations
  def main(args: Array[String]): Unit = {
    val x = 10
    val y = 5
    
    println(s"Addition de $x et $y: ${addition(x, y)}")
    println(s"Soustraction de $x et $y: ${soustraction(x, y)}")
    println(s"Multiplication de $x et $y: ${multiplication(x, y)}")
    division(x, y) match {
      case Some(result) => println(s"Division de $x par $y: $result")
      case None => println("Division par zéro impossible")
    }
  }
}
