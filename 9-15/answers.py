hello_Name: 
public String helloName(String name) {

  return "Hello " + name + "!";

}

make_out_word: 
  public String makeOutWord(String out, String word) {
    return out.substring(0, 2) + word + out.substring(2);
}

first_two:
  public String firstTwo(String str) {

  int len = str.length();

  if (len < 2)

    return str;

  else

    return str.substring(0,2);

}
