void main() {
  String str(String from, String to) => "moves $from -> $to";

  hanoi(int discs, String a, String b, String c) {
    if (discs > 0) {
      print(str(a, c));
      hanoi(discs - 1, a, c, b);
      hanoi(discs - 1, b, a, c);
    }
  }

  hanoi(3, '1', '2', '3');
}
