# Random-Articles-Generator

        schema
        {
            DOI,
            Pub_date,
            Title,
            
            Journal,
            Publisher,

            Authors: array
            Refs: array
            tags: array
            Doc:{
                array di Chapter:{
                    Title,
                    Paragraphs: array di Paragraph{
                        Title,
                        Sections: array di element {// testo o url}

                    }
                }
            }
        }
