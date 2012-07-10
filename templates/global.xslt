<xsl:template match="page" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <html>
  <title><xsl:value-of select="title"/></title>
  <body>
  <h1><xsl:value-of select="title"/></h1>
  <xsl:for-each select="content/tweakable">
    Giggity
  </xsl:for-each>
  </body>
  </html>
</xsl:template>

