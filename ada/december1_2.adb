with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings; use Ada.Strings;
with Ada.Strings.Maps; use Ada.Strings.Maps;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;
with Ada.Command_Line;

procedure December1_2 is
  package Cli renames Ada.Command_Line;
  
  function Replace_Words_For_Numbers (Line : String) return String is
  begin
    return Line;
  end Replace_Words_For_Numbers;

  function Get_Number(Line : String) return Integer is
    Numbers : String (1 .. 2) := "00";
    Index : Integer := 1;
  begin
    for Char of Line loop
      if '0' <= Char and Char <= '9' then
        if Index = 1 then
          Numbers(Index) := Char;
          Numbers(Index + 1) := Char;
          Index := Index + 1;
        else
          Numbers(Index) := Char;
        end if;
      end if;
    end loop;

    return Integer'Value(Numbers);
  end Get_Number;

  F : File_Type;
  Sum : Integer := 0;

begin
  if Cli.Argument_Count = 1 then
    Open(F, In_File, Cli.Argument(1));

    while not End_Of_File(F) loop
      Sum := Sum + Get_Number(Get_Line(F));
    end loop;

    Close(F);

    Put_Line(Integer'Image(Sum));
  else
    Put_Line("Error - Invalid number of arguments: expected (1) <file_name>, got " 
             & Integer'Image(Cli.Argument_Count));
  end if;
end December1_2;
