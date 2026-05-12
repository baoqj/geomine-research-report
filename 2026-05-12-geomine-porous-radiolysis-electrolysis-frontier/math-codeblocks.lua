function CodeBlock(el)
  if el.classes:includes("math") then
    return pandoc.Math("DisplayMath", el.text)
  end
  return nil
end
