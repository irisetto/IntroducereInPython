def build_xml_element(tag, content, **keys): #Operator ** can be used in a function to specify that the list of parameters of that function should be treated as a dictionary.
    xml_element = f"<{tag}"

    #for key, value in keys.items(): #LISTA DE TUPLE
    xml_element +=  " ".join([f' {key}="{value}"' for key, value in keys.items()])

    xml_element += f">{content}</{tag}>"

    return xml_element

def main():
    result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(result)


if __name__ == "__main__":
    main()