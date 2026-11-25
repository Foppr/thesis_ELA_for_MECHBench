import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced polynomial chaos component with fractional exponents and adaptive coefficients
        for i in range(self.dim):
            coeff = 1.5 + 0.5 * np.sin(0.3 * i)
            result += coeff * (x[i]**6.5 + 0.4 * x[i]**5.2 + 0.2 * x[i]**4.1 + 0.05 * x[i]**3.7)
            
        # Modified radial basis function with dynamic widths and shifted centers
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                width1 = 0.4 + 0.1 * np.sin(0.2 * i)
                width2 = 0.3 + 0.05 * np.cos(0.15 * i)
                result += 2.5 * np.exp(-0.5 * (x[i] - centers[i])**2 / width1) + 1.2 * np.exp(-0.3 * (x[i] + centers[i])**2 / width2)
                
        # Enhanced dynamic cross-dimensional coupling with multi-frequency sinusoids
        t = 1.5 + 0.2 * self.dim
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling1 = np.sin(t * x[i] * x[j]) * np.cos(0.3 * t * (x[i]**2 + x[j]**2))
                coupling2 = np.cos(1.5 * t * x[i] * x[j]) * np.sin(0.7 * t * (x[i]**2 - x[j]**2))
                result += 2.0 * (coupling1 + 0.5 * coupling2)
                
        # Improved multi-modal sine-polynomial interactions
        for i in range(self.dim):
            result += 3.0 * np.sin(2.5 * x[i]) * (x[i]**4 - 1.8 * x[i]**2 + 0.8)
            
        # Enhanced fractional power chaotic component with modified frequencies
        for i in range(self.dim):
            result += 2.0 * np.power(np.abs(x[i]), 1.6) * np.sin(6.0 * x[i]) + 0.5 * np.power(np.abs(x[i]), 1.9) * np.cos(4.0 * x[i])
            
        # Improved conditioning factor
        condition_factor = 1.2 + 0.3 * np.log(self.dim + 1)
        result *= condition_factor
        
        # Modified hyperbolic interactions with additional cross terms
        for i in range(self.dim):
            result += 1.5 * np.sinh(1.2 * x[i]) * np.cos(1.8 * x[i]) + 1.0 * np.cosh(1.0 * x[i]) * np.sin(1.5 * x[i])
            
        # Enhanced nested trigonometric component
        for i in range(self.dim):
            nested = 0.0
            for k in range(1, 8):
                nested += 0.25**k * np.sin(2**(k+1) * x[i])
            result += nested
            
        # Modified penalty term with exponential scaling
        result += 0.8 * np.sum(np.exp(np.abs(x) / 2.0) - 1.0)
        
        # Improved multi-modal component with additional harmonic terms
        for i in range(self.dim):
            result += 1.2 * np.exp(-0.3 * x[i]**2) * np.sin(5.0 * x[i]) + 0.3 * np.exp(-0.7 * x[i]**2) * np.cos(3.0 * x[i])
            
        # Enhanced cross-dimensional polynomial coupling with time-varying coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.6 + 0.4 * np.sin(0.2 * (i - j))
                result += coeff * (x[i]**3 + x[j]**3) * np.cos(x[i] * x[j])
                
        # Refined time-varying chaotic modulation
        for i in range(self.dim):
            result += 1.1 * np.sin(np.pi * np.sin(3.5 * x[i])) * np.cos(np.pi * np.cos(2.5 * x[i]))
            
        return result