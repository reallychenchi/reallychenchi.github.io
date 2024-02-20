---
layout: post
title: 大模型使用案例
date: 2024-2-20 23:45
categories: 编程
tags: Chatgpt
---
本文是部分大模型在编程工作中的试用笔记。

 <!-- more -->

- [使用案例](#使用案例)
  - [画界面](#画界面)
    - [提问](#提问)
    - [回答](#回答)
  - [定义数据结构](#定义数据结构)
    - [提问](#提问-1)
    - [回答](#回答-1)
  - [常见算法](#常见算法)
    - [提问](#提问-2)
    - [回答](#回答-2)
    - [小结](#小结)
    - [再次提问](#再次提问)
    - [回答](#回答-3)
    - [小结](#小结-1)
  - [为MarkDown文档生成索引](#为markdown文档生成索引)
    - [提问](#提问-3)
    - [回答](#回答-4)
    - [小结](#小结-2)
- [优化](#优化)
  - [背景](#背景)
  - [WebImageView使用代码的尝试](#webimageview使用代码的尝试)
    - [提问](#提问-4)
    - [回答](#回答-5)
    - [小结](#小结-3)
  - [WebImageView使用样本的提问](#webimageview使用样本的提问)
    - [提问](#提问-5)
    - [回答](#回答-6)
    - [小结](#小结-4)
  - [CustomText第一次尝试](#customtext第一次尝试)
    - [提问](#提问-6)
    - [回答](#回答-7)
    - [小结](#小结-5)
  - [CustomText第二次尝试](#customtext第二次尝试)
    - [提问](#提问-7)
    - [回答](#回答-8)
    - [小结](#小结-6)
  - [CustomText第三次尝试](#customtext第三次尝试)
    - [替换规则提问](#替换规则提问)
    - [替换规则回答](#替换规则回答)
    - [执行代码片段替换提问](#执行代码片段替换提问)
    - [执行代码片段替换回答](#执行代码片段替换回答)
    - [小结](#小结-7)
  - [CustomText第四次尝试](#customtext第四次尝试)
    - [提问](#提问-8)
    - [回答](#回答-9)
    - [小结](#小结-8)
- [总结](#总结)
 
# 使用案例
## 画界面
### 提问
用React Native写一个JSX布局，顶部是一个文本，字号12，字重600，颜色是666E75；然后是标题文本，字号16，行高24，字重700，颜色是14181C；下面是一条分割线，分割线高度1像素，左右没有边距，颜色是D6D8DA，上下边距是20；下面是标题文本，内容是How to use，字号20，行高24，字重500，颜色是14181C；下面是描述文本，允许多行展示，字号14，行高20，字重400；然后下面是一个View，内容为空；View下面是一个按钮，宽度占满，高度52，颜色是AE8F4C，圆角半径是8。注意不要使用inline style，输出代码就可以了不要解释
### 回答
```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
 
const App = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.topText}>Top Text</Text>
      <Text style={styles.titleText}>Title Text</Text>
      <View style={styles.separator} />
      <Text style={styles.titleText}>How to use</Text>
      <Text style={styles.descriptionText}>
        This is a description text that can span multiple lines.
      </Text>
      <View style={styles.viewContainer} />
      <View style={styles.buttonContainer}>
        <Text style={styles.buttonText}>Button</Text>
      </View>
    </View>
  );
};
 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  topText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#666E75',
  },
  titleText: {
    fontSize: 16,
    lineHeight: 24,
    fontWeight: '700',
    color: '#14181C',
  },
  separator: {
    height: 1,
    backgroundColor: '#D6D8DA',
    marginVertical: 20,
  },
  descriptionText: {
    fontSize: 14,
    lineHeight: 20,
    fontWeight: '400',
  },
  viewContainer: {},
  buttonContainer: {
    width: '100%',
    height: 52,
    backgroundColor: '#AE8F4C',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});
 
export default App;
```

## 定义数据结构
### 提问
写一个typescript数据结构，描述如下json：
{
"id": "1db2e761-3ee5-46ed-82d5-46847aacf4e9",
"name": "Wealth",
"imageName": "Wealth.png",
"imageLink": "",
"color": "Blue",
"createdAt": "2023-12-01T07:03:58.662Z",
"updatedAt": "2023-12-01T07:03:58.662Z"
}
### 回答
```jsx
interface Wealth {
 id: string;
 name: string;
 imageName: string;
 imageLink: string;
 color: string;
 createdAt: Date;
 updatedAt: Date;
}
```
在这个例子中，我们定义了一个名为`Wealth`的接口，它包含了一个`id`属性，一个`name`属性，一个`imageName`属性，一个`imageLink`属性，一个`color`属性，一个`createdAt`属性，一个`updatedAt`属性。这些属性的类型都是字符串或日期。

你可以使用这个接口来描述JSON数据，例如：
```jsx
const wealth: Wealth = {
 id: "1db2e761-3ee5-46ed-82d5-46847aacf4e9",
 name: "Wealth",
 imageName: "Wealth.png",
 imageLink: "",
 color: "Blue",
 createdAt: new Date("2023-12-01T07:03:58.662Z"),
 updatedAt: new Date("2023-12-01T07:03:58.662Z")
};
```
在这个例子中，我们使用了`Wealth`接口来描述JSON数据，并且使用了`new Date()`函数来创建`createdAt`和`updatedAt`属性的值。。

## 常见算法
### 提问
有数组
"applicableTier": [
    "2",
    "1"
] 写一个typescript函数，返回这个数组最大的数字+1

```jsx
function getNextApplicableTier(applicableTier: string[]): number {
 return Math.max(...applicableTier) + 1;
}
```
在这个例子中，我们定义了一个名为`getNextApplicableTier`的函数，它接受一个名为`applicableTier`的数组作为参数。这个函数使用了`Math.max()`函数来获取数组中的最大值，并且使用了`+ 1`操作符来获取下一个可用的层级。
### 回答
你可以使用这个函数来获取下一个可用的层级，例如：
```
const applicableTier = ["2", "1"];
const nextApplicableTier = getNextApplicableTier(applicableTier);
console.log(nextApplicableTier); // Output: 3
```
在这个例子中，我们使用了`getNextApplicableTier`函数来获取下一个可用的层级，并且使用了`console.log()`函数来打印出结果。。
### 小结
使用时候发现给出的函数运行报错

### 再次提问

"applicableTier": [
"2",
"1"
] 写一个typescript函数，返回这个数组最大的数字+1，注意string 和number之间类型转换问题
### 回答
```
function getNextApplicableTier(applicableTier: string[]): number {
 return Math.max(...applicableTier.map(Number)) + 1;
}
```
在这个例子中，我们使用了`map()`方法来将数组中的每个元素转换为数字，然后使用了`Math.max()`函数来获取数组中的最大值，并且使用了`+ 1`操作符来获取下一个可用的层级。

你可以使用这个函数来获取下一个可用的层级，例如：
```
const applicableTier = ["2", "1"];
const nextApplicableTier = getNextApplicableTier(applicableTier);
console.log(nextApplicableTier); // Output: 3
```
在这个例子中，我们使用了`getNextApplicableTier`函数来获取下一个可用的层级，并且使用了`console.log()`函数来打印出结果。。

请注意，在这个例子中，我们使用了`map()`方法来将数组中的每个元素转换为数字，这样可以避免类型转换问题。。
### 小结
这次没问题了
## 为MarkDown文档生成索引
### 提问
write a python script, read an markdown document, and output the "table of content" of the markdown document. in the format of link
### 回答
To generate a table of contents in the form of links, we need to extract the headers and their corresponding links. Here's a Python script that uses the `re` module to find the headers in a Markdown document and generates a table of contents in the form of links.

```python
import re

def extract_toc(filename):
    with open(filename, 'r') as file:
        content = file.read()

    headers = re.findall(r'^(#+)\s+(.+)', content, re.MULTILINE)

    toc = []
    for level, header in headers:
        link = '-'.join(header.lower().split())  # Generate a link from the header
        toc.append((len(level), (header, link)))

    return toc

def print_toc(toc):
    for level, (header, link) in toc:
        print('    ' * (level - 1) + f'- [{header}](#{link})')

if __name__ == "__main__":
    toc = extract_toc('your_markdown_file.md')
    print_toc(toc)
```

This script reads a Markdown file, finds all headers in the file, and prints them out in a table of contents-like format in the form of links. The depth of the header (i.e., the number of `#` characters at the start of the line) is used to determine the indentation level.

Please replace `'your_markdown_file.md'` with the path to your Markdown file.

Note: This script does not handle nested headers or headers with the same text. If you need to handle these cases, you would need a more complex regular expression or a more sophisticated parsing algorithm.
<|EOT|>

### 小结
本文的索引就是使用上述python脚本生成，没有做任何修改，有点小问题，不过效果很好

# 优化
## 背景
在aia+开发过程中，我们提供了很多组件来代替常见组件，比如用CustomText代替Text。但是这样的代替有时候需要把Text一个个找出来替换掉，非常麻烦，有没有可能让Ai代替我们做这件事？
## WebImageView使用代码的尝试
### 提问
我们自定义了一个WebImageView组件代替React Native的Image组件，它的代码是这样的：
```jsx
/* eslint-disable react-native/no-inline-styles */
import React from 'react';
import {
  Image,
  ImageResizeMode,
  StyleProp,
  ImageStyle,
  View,
} from 'react-native';
import Images from '../../assets/Images';

export interface IWebImageViewProps {
  size?: { width: number | string; height: number | string };
  imgUrl?: string;
  placeHolder: 'big' | 'small' | '';
  resizeMode?: ImageResizeMode | undefined;
  customStyle?: StyleProp<ImageStyle>;
}

export const WebImageView: React.FC<IWebImageViewProps> = (
  props: IWebImageViewProps
) => {
  const { size, resizeMode, imgUrl, customStyle, placeHolder } = props;
  return (
    <View
      style={[
        {
          width: size?.width,
          height: size?.height,
          overflow: 'hidden',
        },
        customStyle,
      ]}
    >
      <Image
        source={{
          uri: imgUrl,
        }}
        defaultSource={
          placeHolder === 'small'
            ? Images.common.com_coupon
            : Images.common.bg_placeholder
        }
        resizeMode={resizeMode}
        onError={(error) => {
          console.log(error);
        }}
        onLoad={() => {
          console.log('onload');
        }}
        onLoadEnd={() => {
          console.log('onloadend');
        }}
        style={[
          {
            width: size?.width,
            height: size?.height,
          },
          customStyle,
        ]}
      />
    </View>
  );
};
```

请完成下列代码的替换：
1、
```jsx
       <Image
          source={imgUrl}
          style={styles.headerImage}
          resizeMode="cover"
          onError={() => setImgUrl(Images.common.empty_photo)}
        />
```

2、
```jsx
      <Image
        style={{
          height: BACKGROUND_HEIGHT,
          backgroundColor: colors.surfaceDigitalred,
        }}
        source={{
          uri: rewardDetails?.display_img_url,
        }}
        resizeMode={'center'}
      />
```

3、 
```jsx
     <Image
        style={{
          marginTop: -500,
          height: BACKGROUND_HEIGHT + 500,
          backgroundColor: colors.surfaceWhite,
        }}
        source={{
          uri: rewardDetails?.display_img_url,
        }}
      />
```
### 回答
Here are the completed code replacements:

1.
```jsx
<WebImageView
customStyle={styles.headerImage}
placeHolder="small"
resizeMode="cover"
imgUrl={imgUrl}
onError={() => setImgUrl(Images.common.empty_photo)}
/>
```

2. 
```jsx
<WebImageView
size={{
width: '100%',
height: BACKGROUND_HEIGHT,
}}
placeHolder="big"
resizeMode="center"
imgUrl={rewardDetails?.display_img_url}
/>
```

1. 
```jsx
<WebImageView
size={{
width: '100%',
height: BACKGROUND_HEIGHT + 500,
}}
placeHolder="big"
resizeMode="cover"
imgUrl={rewardDetails?.display_img_url}
/>
```

Please note that the WebImageView component must exist in your project for these code replacements to work..

### 小结
基本正确，出现个别问题属于可以接受的。

## WebImageView使用样本的提问
### 提问
参考下面代码示范，然后对指定代码段进行修改：
示范1:
原代码：
```jsx
          <Image
            style={{
              marginBottom: Spacing['space-3'],
              resizeMode: resizeMode,
              width: 58,
            }}
            source={{ uri: imgUrl }}
          />
```
改为：
```jsx
          <WebImageView
            customStyle={{
              marginBottom: Spacing['space-3'],
              height: 58,
              borderRadius: 8,
            }}
            placeHolder="small"
            resizeMode={resizeMode}
            size={{ height: 58, width: 112 }}
            imgUrl={imgUrl}
          />
```

示范2:
原代码：
```jsx
        <Image
          style={styles.imageStyle}
          source={{ uri: icon }}
          resizeMode="cover"
        />
```
改为：
```jsx
<WebImageView
          customStyle={styles.imageStyle}
          imgUrl={icon}
          size={{
            width: '100%',
            height: 72,
          }}
          placeHolder="small"
          resizeMode="cover"
        />
```

示范3:
原代码：
```jsx
<Image
        style={{
          marginTop: -500,
          height: BACKGROUND_HEIGHT + 500,
          backgroundColor: colors.surfaceWhite,
        }}
        source={{
          uri:
            'https://s7ap1.scene7.com/is/image/aia/sonxaiav3?qlt=85&wid=1600&ts=1690523644929&dpr=off',
        }}
      />
```
改为：
```jsx
<WebImageView
          size={{
            height: '100%',
            width: '100',
          }}
          placeHolder="big"
          resizeMode="cover"
          imgUrl={
            'https://s7ap1.scene7.com/is/image/aia/sonxaiav3?qlt=85&wid=1600&ts=1690523644929&dpr=off'
          }
        />
```

要求按照前面三个示范，修改下列代码：
```jsx
        <Image
          source={imgUrl}
          style={[styles.image, { height: imgHeight }]}
          resizeMode="cover"
        />
```

### 回答
Here is the modified code based on the examples provided:
```jsx

<WebImageView
 customStyle={[styles.image, { height: imgHeight }]}
 placeHolder="small"
 resizeMode="cover"
 imgUrl={imgUrl}
/>
```

Please note that the WebImageView component must exist in your project for this code to run..

### 小结
主要是提供样本太麻烦了，输出结果还可以。

## CustomText第一次尝试
给出规则和文件，要求ai在文件当中完成替换以后输出文件。
### 提问
eact native当中，我们要使用一个CustomText 替换Text，替换的规则是：
1、all the text nodes which wrapped inside of a <Text> component should be put in text parameter of CustomText, and CustomText should not wrapped them.
2、style替换成customStyle
3、color替换成textColor
4、CustomText 不应该包含任何子元素，任何被Text包含的元素，要放在customText的text参数里面。
例如：
```jsx
   <Text variant="body-3-regular" color={colors.textDefault}>
              {'Valid till '}
            </Text>
```
要改成：
```jsx
            <CustomText variant="body-3-regular" textColor={colors.textDefault}
text="Valid till "
/>
```
按照上述原则，把下面文件当中的 Text替换成CustomText，然后输出整个文件

```jsx
/* eslint-disable react-native/no-inline-styles */
import {
  View,
  StyleProp,
  ViewStyle,
  ViewProps,
  Image,
  ImageBackground,
  ImageSourcePropType,
  TouchableOpacity,
  ImageResizeMode,
} from 'react-native';
import React from 'react';
import { ddsTheme } from '../../config/themeConfig';
import Images from '../../assets/Images';
import Text from '@aia-mobile-dds/atoms/Text/Text';
import DashLine from '../DashLine/DashLine';
import { Spacing } from '@aia-mobile-dds/hooks/Spacing';
import CustomText from '../CustomText';
import { WebImageView } from '../WebImageView';

const { colors } = ddsTheme;
export interface ICouponViewProps extends ViewProps {
  otherStyle?: StyleProp<ViewStyle> | undefined;
  image?: ImageSourcePropType;
  imgUrl?: string;
  title: string;
  content: string;
  date: string;
  imageWidth?: number;
  resizeMode?: ImageResizeMode | undefined;
  isLongCoupon?: boolean;
  onPress?: () => void;
}

export const CouponView: React.FC<ICouponViewProps> = (
  props: ICouponViewProps
) => {
  const {
    otherStyle,
    title,
    image,
    imgUrl,
    content,
    date,
    imageWidth = 112,
    isLongCoupon = false,
    resizeMode = 'contain',
    onPress,
  } = props;
  console.log('imageUrl=====', imgUrl);

  return (
    <TouchableOpacity onPress={onPress}>
      <ImageBackground
        style={[
          {
            width: 144,
            height: isLongCoupon ? 192 : 172,
            padding: Spacing['space-4'],
            alignItems: 'center',
          },
          otherStyle,
        ]}
        resizeMode={'stretch'}
        source={
          isLongCoupon
            ? Images.wallet.vitality_coupon_bgLong
            : Images.wallet.vitality_coupon_bg
        }
        {...props}
      >
        {image && (
          <Image
            style={{
              marginBottom: Spacing['space-3'],
              width: imageWidth,
              height: 58,
              resizeMode: resizeMode,
            }}
            source={image}
          />
        )}
        {imgUrl && (
          <WebImageView
            customStyle={{
              marginBottom: Spacing['space-3'],
              width: imageWidth,
              height: 58,
              borderRadius: 8,
            }}
            placeHolder="small"
            resizeMode={resizeMode}
            size={{ height: 58, width: 112 }}
            imgUrl={imgUrl}
          />
        )}

        <DashLine
          otherStyle={{ marginTop: 0 }}
          windowWidth={14}
          lineHeight={1}
          lineWidth={2}
        />

        <View style={isLongCoupon ? { flex: 1, height: 106 } : undefined}>
          <CustomText
            variant="body-3-semibold"
            textColor={colors.textSubdued}
            text={title}
            numberOfLines={1}
            customStyle={{
              marginTop: 8,
            }}
          />

          <Text
            variant="body-2-bold"
            color={colors.textDefault}
            numberOfLines={isLongCoupon ? 2 : 1}
            customStyle={{
              marginTop: 4,
              marginBottom: 6,
              height: isLongCoupon ? 40 : 20,
            }}
          >
            {content}
          </Text>
          <View
            style={{
              flexDirection: 'row',
              marginBottom: 16,
            }}
          >
            <Text variant="body-3-regular" color={colors.textDefault}>
              {'Valid till '}
            </Text>
            <Text variant="body-3-semibold" color={colors.textDefault}>
              {date}
            </Text>
          </View>
        </View>
      </ImageBackground>
    </TouchableOpacity>
  );
};
```
### 回答
Here is the code with all the Text components replaced with CustomText components:

```jsx
/* eslint-disable react-native/no-inline-styles */
import {
  View,
  StyleProp,
  ViewStyle,
  ViewProps,
  Image,
  ImageBackground,
  ImageSourcePropType,
  TouchableOpacity,
  ImageResizeMode,
} from 'react-native';
import React from 'react';
import { ddsTheme } from '../../config/themeConfig';
import Images from '../../assets/Images';
import CustomText from '../CustomText';
import DashLine from '../DashLine/DashLine';
import { Spacing } from '@aia-mobile-dds/hooks/Spacing';
import { WebImageView } from '../WebImageView';

const { colors } = ddsTheme;
export interface ICouponViewProps extends ViewProps {
  otherStyle?: StyleProp<ViewStyle> | undefined;
  image?: ImageSourcePropType;
  imgUrl?: string;
  title: string;
  content: string;
  date: string;
  imageWidth?: number;
  resizeMode?: ImageResizeMode | undefined;
  isLongCoupon?: boolean;
  onPress?: () => void;
}

export const CouponView: React.FC<ICouponViewProps> = (
  props: ICouponViewProps
) => {
  const {
    otherStyle,
    title,
    image,
    imgUrl,
    content,
    date,
    imageWidth = 112,
    isLongCoupon = false,
    resizeMode = 'contain',
    onPress,
  } = props;
  console.log('imageUrl=====', imgUrl);

  return (
    <TouchableOpacity onPress={onPress}>
      <ImageBackground
        style={[
          {
            width: 144,
            height: isLongCoupon ? 192 : 172,
            padding: Spacing['space-4'],
            alignItems: 'center',
          },
          otherStyle,
        ]}
        resizeMode={'stretch'}
        source={
          isLongCoupon
            ? Images.wallet.vitality_coupon_bgLong
            : Images.wallet.vitality_coupon_bg
        }
        {...props}
      >
        {image && (
          <Image
            style={{
              marginBottom: Spacing['space-3'],
              width: imageWidth,
              height: 58,
              resizeMode: resizeMode,
            }}
            source={image}
          />
        )}
        {imgUrl && (
          <WebImageView
            customStyle={{
              marginBottom: Spacing['space-3'],
              width: imageWidth,
              height: 58,
              borderRadius: 8,
            }}
            placeHolder="small"
            resizeMode={resizeMode}
            size={{ height: 58, width: 112 }}
            imgUrl={imgUrl}
          />
        )}

        <DashLine
          otherStyle={{ marginTop: 0 }}
          windowWidth={14}
          lineHeight={1}
          lineWidth={2}
        />

        <View style={isLongCoupon ? { flex: 1, height: 106 } : undefined}>
          <CustomText
            variant="body-3-semibold"
            textColor={colors.textSubdued}
            text={title}
            numberOfLines={1}
            customStyle={{
              marginTop: 8,
            }}
          />

          <CustomText
            variant="body-2-bold"
            textColor={colors.textDefault}
            numberOfLines={isLongCoupon ? 2 : 1}
            customStyle={{
              marginTop: 4,
              marginBottom: 6,
              height: isLongCoupon ? 40 : 20,
            }}
          >
            {content}
          </CustomText>
          <View
            style={{
              flexDirection: 'row',
              marginBottom: 16,
            }}
          >
            <CustomText variant="body-3-regular" textColor={colors.textDefault} text="Valid till " />
            <CustomText variant="body-3-semibold" textColor={colors.textDefault}>
              {date}
            </CustomText>
          </View>
        </View>
      </ImageBackground>
    </TouchableOpacity>
  );
};
```

Please note that the CustomText component must exist in your project for this code to run.
<|EOT|>

### 小结
出现了明显错误，主要在于对与Text wrapped的替换理解不到位，总是在这方面犯错误，忘记把wrapped text改为text参数形式。
在多次修改提示词以后，仍然没有改进。

## CustomText第二次尝试
给出规则和代码片段，要求ai在文件当中完成替换以后输出替换以后的代码片段。
### 提问
there is a new text called CustomText which is used to replace text. The main difference is that CustomText accepts only string in parameter text, but Text accepts string by wrap them. Such as :
```jsx
<Text>some thing</Text>
```

should write like
```jsx
<CustomText text="some thing"/>
```
And some other rules:

style should be replaced as customStyle
color should be replaced as textColor
Replace the Text to CustomText in following code:

```jsx
          <Text
            variant="body-2-bold"
            color={colors.textDefault}
            numberOfLines={isLongCoupon ? 2 : 1}
            style={{
              marginTop: 4,
              marginBottom: 6,
              height: isLongCoupon ? 40 : 20,
            }}
          >
            {content}
          </Text>
```
### 回答
Here is the updated code with the `CustomText` component:
```jsx
          <CustomText
            variant="body-2-bold"
            textColor={colors.textDefault}
            text={content}
            numberOfLines={isLongCoupon ? 2 : 1}
            customStyle={{
              marginTop: 4,
              marginBottom: 6,
              height: isLongCoupon ? 40 : 20,
            }}
          />
```
In this code, we have replaced the `Text` component with `CustomText` in the `content` prop.

Note that we have also updated the `CustomText` component to use the `text` prop instead of the `children` prop, and we have passed the `content` variable as the value of the `text` prop.

Additionally, we have updated the `CustomText` component to use the `textColor` prop instead of the `color` prop, and we have passed the `colors.textDefault` variable as the value of the `textColor` prop.

This should replace the `Text` component with the `CustomText` component in the code you provided..

### 小结
回答的很好，和前面比起来进步很大。很可能是因为输入、输出的长度影响导致的。所以我们在输入输出的时候应该尽量短一些。
AI的表现，受到输入输出长短影响也是业界普遍现象。

## CustomText第三次尝试
给出CustomText源码，要求ai自己输出替换规则，ai使用自己给出的替换规则对代码片断进行替换，从而实现“自动重构”。当然过程还是有人参与的，但是相信适当增加辅助胶水代码以后，可以实现全自动。
### 替换规则提问
This is a new CustomText component, it is used to replace the common Text react native component, please give out rule for replacement.
```jsx
import Text from '@aia-mobile-dds/atoms/Text';
import { InAppBrowserService } from '@aiaplus/mobile-utils';
import React from 'react';
import { StyleProp, StyleSheet, TextStyle } from 'react-native';
import { ddsTheme } from '../../config/themeConfig';

interface IProps {
  onPress?: (innerText?: string) => void;
  text?: string;
  customStyle?: StyleProp<TextStyle>;
  partsStyle?: StyleProp<TextStyle>;
  variant?: string;
  aVariant?: string;
  bVariant?: string;
  cVariant?: string;
  textColor?: string;
  aLabelColor?: string;
  bLabelColor?: string;
  cLabelColor?: string;
  numberOfLines?: number;
  ellipsizeMode?: 'head' | 'middle' | 'tail' | 'clip';
}
const { colors } = ddsTheme;
const CustomText: React.FC<IProps> = (props) => {
  const {
    onPress,
    text = '',
    customStyle,
    partsStyle,
    variant = 'body-2-regular',
    aVariant = 'body-2-regular',
    bVariant = 'body-2-semibold',
    cVariant = 'body-2-semibold',
    textColor = colors.textDefault,
    aLabelColor = colors.textDefault,
    bLabelColor = colors.textDefault,
    cLabelColor = colors.textDefault,
    numberOfLines,
    ellipsizeMode,
  } = props;

  const parts = () => {
    let newText = text;
    if (newText.includes('<p>') && newText.includes('</p>')) {
      newText = newText.replaceAll('<p>', '');
      newText = newText.replaceAll('</p>', '');
    }
    return newText?.split(/(<[a-zA-Z].*?>[^<>]+<\/[a-zA-Z]>)/);
  };
  const textElements = parts().map((part, index) => {
    if (part.trim() === '') return;
    if (part.startsWith('<')) {
      const tag = part.substring(1, 2);
      const innerText = part
        .split(/<\/?[abcp]>/g)
        .filter((item) => item.length > 0)[0];
      switch (tag) {
        case 'a':
          const linkRegex = /<a\s+href=['"]([^"]+)['"]\s*>([^<]+)<\/a>/;
          // /<a href="([^"]+)">([^<]+)<\/a>/g;
          const match = linkRegex.exec(part);
          let linkText;
          let clickLink: any;
          if (match) {
            linkText = match ? match[2] : part;
            clickLink = match ? match[1] : null;
          } else {
            linkText = part.split(/<\/?[abc]>/g)[1];
          }
          return (
            <Text
              variant={aVariant}
              color={aLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              customStyle={styles.customStyle}
              onPress={() => {
                if (onPress) {
                  onPress();
                } else {
                  InAppBrowserService.open(clickLink);
                }
              }}
            >
              {linkText}
            </Text>
          );

        case 'b':
          return (
            <Text
              variant={bVariant}
              color={bLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              onPress={() => {
                onPress && onPress(innerText);
              }}
            >
              {innerText}
            </Text>
          );
        case 'c':
          return (
            <Text
              variant={cVariant}
              color={cLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              customStyle={styles.customStyle}
              onPress={() => {
                onPress && onPress(innerText);
              }}
            >
              {innerText}
            </Text>
          );
        case 'p':
          return (
            <Text
              color={textColor}
              key={index}
              customStyle={partsStyle}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
            >
              {innerText}
            </Text>
          );
        default:
          return (
            <Text
              customStyle={partsStyle}
              variant={variant}
              color={textColor}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              key={index}
            >
              {part}
            </Text>
          );
      }
    } else {
      return (
        <Text
          customStyle={partsStyle}
          variant={variant}
          color={textColor}
          key={index}
        >
          {part}
        </Text>
      );
    }
  });

  return (
    <Text
      customStyle={customStyle}
      numberOfLines={numberOfLines}
      ellipsizeMode={ellipsizeMode}
    >
      {textElements}
    </Text>
  );
};

export default CustomText;

const styles = StyleSheet.create({
  customStyle: {
    textDecorationLine: 'underline',
  },
});
```

### 替换规则回答
The `CustomText` component is a custom component that replaces the `Text` component from React Native. It accepts a `text` prop that contains the text to be displayed, and it also accepts several other props that can be used to customize the appearance of the text.

Here are the rules for replacing the `Text` component with the `CustomText` component:

1. Replace the `Text` component with the `CustomText` component in the code.
2. Pass the `text` prop to the `CustomText` component, and set it to the value of the `text` variable.
3. If the `CustomText` component has any other props that you want to set, you can pass them to the component as well. For example, if you want to set the `variant` prop to a specific value, you can pass it to the `CustomText` component like this: `<CustomText variant="body-2-regular">`.
4. If you want to set the `customStyle` prop to a specific value, you can pass it to the `CustomText` component like this: `<CustomText customStyle={{ textDecorationLine: 'underline' }}>`.
5. If you want to set the `numberOfLines` prop to a specific value, you can pass it to the `CustomText` component like this: `<CustomText numberOfLines={2}>`.
6. If you want to set the `ellipsizeMode` prop to a specific value, you can pass it to the `CustomText` component like this: `<CustomText ellipsizeMode="tail">`.

Here is an example of how you can replace the `Text` component with the `CustomText` component in the code:
```jsx
import CustomText from './CustomText';

const MyComponent = () => {
 const text = 'This is a custom text component';

 return (
    <CustomText text={text} variant="body-2-regular" customStyle={{ textDecorationLine: 'underline' }} numberOfLines={2} ellipsizeMode="tail" />
 );
};
```
In this example, we have replaced the `Text` component with the `CustomText` component, and we have passed the `text` variable as the value of the `text` prop. We have also set the `variant` prop to `"body-2-regular"`, the `customStyle` prop to `{{ textDecorationLine: 'underline' }}`, the `numberOfLines` prop to `2`, and the `ellipsizeMode` prop to `"tail"`.....

### 执行代码片段替换提问
Here are the rules for replacing the Text component with the CustomText component:

Replace the Text component with the CustomText component in the code.
Pass the text prop to the CustomText component, and set it to the value of the text variable.
If the CustomText component has any other props that you want to set, you can pass them to the component as well. For example, if you want to set the variant prop to a specific value, you can pass it to the CustomText component like this: <CustomText variant="body-2-regular">.
If you want to set the customStyle prop to a specific value, you can pass it to the CustomText component like this: <CustomText customStyle={{ textDecorationLine: 'underline' }}>.
If you want to set the numberOfLines prop to a specific value, you can pass it to the CustomText component like this: <CustomText numberOfLines={2}>.
If you want to set the ellipsizeMode prop to a specific value, you can pass it to the CustomText component like this: <CustomText ellipsizeMode="tail">.

fowlling the above instructions, replace the below <Text/> to <CustomText/>

```jsx
<Text
        variant="body-2-bold"
        color={colors.textDefault}
        numberOfLines={isLongCoupon ? 2 : 1}
        style={{
          marginTop: 4,
          marginBottom: 6,
          height: isLongCoupon ? 40 : 20,
        }}
      >
        {content}
      </Text>
```

### 执行代码片段替换回答
Here is the updated code with the `CustomText` component:
```jsx
<CustomText
        variant="body-2-bold"
        textColor={colors.textDefault}
        text={content}
        numberOfLines={isLongCoupon ? 2 : 1}
        customStyle={{
          marginTop: 4,
          marginBottom: 6,
          height: isLongCoupon ? 40 : 20,
        }}
      />
```
In this code, we have replaced the `Text` component with the `CustomText` component in the `content` prop.

Note that we have also updated the `CustomText` component to use the `text` prop instead of the `children` prop, and we have passed the `content` variable as the value of the `text` prop.

Additionally, we have updated the `CustomText` component to use the `textColor` prop instead of the `color` prop, and we have passed the `colors.textDefault` variable as the value of the `textColor` prop.

This should replace the `Text` component with the `CustomText` component in the code you provided..

### 小结
运行结果很好！

## CustomText第四次尝试
给出CustomText源码，直接要求ai一步到位替换代码

### 提问
This is a new CustomText component, it is used to replace the common Text react native component. Read code first:

```jsx
import Text from '@aia-mobile-dds/atoms/Text';
import { InAppBrowserService } from '@aiaplus/mobile-utils';
import React from 'react';
import { StyleProp, StyleSheet, TextStyle } from 'react-native';
import { ddsTheme } from '../../config/themeConfig';

interface IProps {
  onPress?: (innerText?: string) => void;
  text?: string;
  customStyle?: StyleProp<TextStyle>;
  partsStyle?: StyleProp<TextStyle>;
  variant?: string;
  aVariant?: string;
  bVariant?: string;
  cVariant?: string;
  textColor?: string;
  aLabelColor?: string;
  bLabelColor?: string;
  cLabelColor?: string;
  numberOfLines?: number;
  ellipsizeMode?: 'head' | 'middle' | 'tail' | 'clip';
}
const { colors } = ddsTheme;
const CustomText: React.FC<IProps> = (props) => {
  const {
    onPress,
    text = '',
    customStyle,
    partsStyle,
    variant = 'body-2-regular',
    aVariant = 'body-2-regular',
    bVariant = 'body-2-semibold',
    cVariant = 'body-2-semibold',
    textColor = colors.textDefault,
    aLabelColor = colors.textDefault,
    bLabelColor = colors.textDefault,
    cLabelColor = colors.textDefault,
    numberOfLines,
    ellipsizeMode,
  } = props;

  const parts = () => {
    let newText = text;
    if (newText.includes('<p>') && newText.includes('</p>')) {
      newText = newText.replaceAll('<p>', '');
      newText = newText.replaceAll('</p>', '');
    }
    return newText?.split(/(<[a-zA-Z].*?>[^<>]+<\/[a-zA-Z]>)/);
  };
  const textElements = parts().map((part, index) => {
    if (part.trim() === '') return;
    if (part.startsWith('<')) {
      const tag = part.substring(1, 2);
      const innerText = part
        .split(/<\/?[abcp]>/g)
        .filter((item) => item.length > 0)[0];
      switch (tag) {
        case 'a':
          const linkRegex = /<a\s+href=['"]([^"]+)['"]\s*>([^<]+)<\/a>/;
          // /<a href="([^"]+)">([^<]+)<\/a>/g;
          const match = linkRegex.exec(part);
          let linkText;
          let clickLink: any;
          if (match) {
            linkText = match ? match[2] : part;
            clickLink = match ? match[1] : null;
          } else {
            linkText = part.split(/<\/?[abc]>/g)[1];
          }
          return (
            <Text
              variant={aVariant}
              color={aLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              customStyle={styles.customStyle}
              onPress={() => {
                if (onPress) {
                  onPress();
                } else {
                  InAppBrowserService.open(clickLink);
                }
              }}
            >
              {linkText}
            </Text>
          );

        case 'b':
          return (
            <Text
              variant={bVariant}
              color={bLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              onPress={() => {
                onPress && onPress(innerText);
              }}
            >
              {innerText}
            </Text>
          );
        case 'c':
          return (
            <Text
              variant={cVariant}
              color={cLabelColor}
              key={index}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              customStyle={styles.customStyle}
              onPress={() => {
                onPress && onPress(innerText);
              }}
            >
              {innerText}
            </Text>
          );
        case 'p':
          return (
            <Text
              color={textColor}
              key={index}
              customStyle={partsStyle}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
            >
              {innerText}
            </Text>
          );
        default:
          return (
            <Text
              customStyle={partsStyle}
              variant={variant}
              color={textColor}
              numberOfLines={numberOfLines}
              ellipsizeMode={ellipsizeMode}
              key={index}
            >
              {part}
            </Text>
          );
      }
    } else {
      return (
        <Text
          customStyle={partsStyle}
          variant={variant}
          color={textColor}
          key={index}
        >
          {part}
        </Text>
      );
    }
  });

  return (
    <Text
      customStyle={customStyle}
      numberOfLines={numberOfLines}
      ellipsizeMode={ellipsizeMode}
    >
      {textElements}
    </Text>
  );
};

export default CustomText;

const styles = StyleSheet.create({
  customStyle: {
    textDecorationLine: 'underline',
  },
});
```


please replace the follow text component to CustomText.
```jsx
<Text
variant="body-2-bold"
color={colors.textDefault}
numberOfLines={isLongCoupon ? 2 : 1}
style={{
marginTop: 4,
marginBottom: 6,
height: isLongCoupon ? 40 : 20,
}}
>
{content}</Text>
```

### 回答

Here is the updated code with the `CustomText` component:
```jsx
<CustomText
 variant="body-2-bold"
 textColor={colors.textDefault}
 text={content}
 numberOfLines={isLongCoupon ? 2 : 1}
 customStyle={{
    marginTop: 4,
    marginBottom: 6,
    height: isLongCoupon ? 40 : 20,
 }}
/>
```
In this code, we have replaced the `Text` component with the `CustomText` component in the `content` prop.

Note that we have also updated the `CustomText` component to use the `text` prop instead of the `children` prop, and we have passed the `content` variable as the value of the `text` prop.

Additionally, we have updated the `CustomText` component to use the `textColor` prop instead of the `color` prop, and we have passed the `colors.textDefault` variable as the value of the `textColor` prop.

This should replace the `Text` component with the `CustomText` component in the code you provided..

### 小结
效果一样很好！从代码直接跨越过来，这么长代码表现还很好。

# 总结
* 输入越长，AI的理解能力就越差。这也是市面上常见AI产品共同表现，我们的ai也是类似。
* 建议在输入上按照chatGpt不要超过4096 token，避免大段代码输入，例如输入代码的时候，只保留关键的接口部分。
* 在输出上也尽量寻求一个尽量简短的输出，从目前有限的实验来看，较长的输出似乎比较长的输入对Ai表现水平影响更大。
* 使用规则描述更好，Ai可以充分理解代码和规则，甚至可以通过 code -> 规则 -> 重构 的方式让ai自动完成较为复杂的重构。
* 小样本学习的主要问题在于我们提供出足够样本的成本太高了，不建议使用。
* 平时的工作生活中多想着点Ai，能用则用，会有惊喜的，比如本文的目录。
