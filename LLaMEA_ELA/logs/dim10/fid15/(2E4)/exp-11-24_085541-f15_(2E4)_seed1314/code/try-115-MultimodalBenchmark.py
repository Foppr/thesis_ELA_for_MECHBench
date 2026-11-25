import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Polynomial chaos component with varying exponents and chaotic modulation
        for i in range(self.dim):
            result += 3.0 * (x[i]**7 + 0.6 * x[i]**6 + 0.4 * x[i]**5 + 0.2 * x[i]**4 + 0.1 * x[i]**3)
            
        # Radial basis function with dynamic centers, widths, and chaotic amplitudes
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                amplitude1 = 2.5 + 0.5 * np.sin(0.3 * i)
                amplitude2 = 2.0 + 0.3 * np.cos(0.4 * i)
                result += amplitude1 * np.exp(-0.6 * (x[i] - centers[i])**2) + amplitude2 * np.exp(-0.4 * (x[i] + centers[i])**2)
                
        # Dynamic cross-dimensional coupling with time-varying sinusoids and chaotic coefficients
        t = 1.5 + 0.2 * self.dim  # Time parameter
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                coeff = 2.2 + 0.9 * np.sin(0.2 * (i + j) * t)  # Slightly increased coefficient
                coupling = coeff * np.sin(t * x[i] * x[j]) * np.cos(0.6 * t * (x[i]**2 + x[j]**2))
                result += coupling
                
        # Multi-modal sine-polynomial interactions with chaotic frequency modulation
        for i in range(self.dim):
            freq_mod = 3.7 + 0.5 * np.sin(0.2 * i)  # Increased frequency modulation
            result += 3.0 * np.sin(freq_mod * x[i]) * (x[i]**5 - 2.5 * x[i]**3 + 1.5 * x[i])
            
        # Fractional power chaotic component with dynamic exponents
        for i in range(self.dim):
            exp = 1.9 + 0.3 * np.sin(0.1 * i)  # Slightly increased exponent
            result += 2.0 * np.power(np.abs(x[i]), exp) * np.sin(6.0 * x[i])
            
        # Adaptive conditioning based on dimensionality with chaotic scaling
        condition_factor = 1.6 + 0.7 * np.log(self.dim + 1) + 0.2 * np.sin(0.3 * self.dim)  # Slightly increased factor
        result *= condition_factor
        
        # Complex hyperbolic interactions with time-varying parameters
        for i in range(self.dim):
            param1 = 1.9 + 0.4 * np.sin(0.2 * i)  # Increased parameter
            param2 = 2.6 + 0.3 * np.cos(0.1 * i)  # Increased parameter
            result += param1 * np.sinh(param2 * x[i]) * np.cos(2.5 * x[i]) + param2 * np.cosh(param1 * x[i]) * np.sin(2.2 * x[i])
            
        # Nested trigonometric component with recursive structure and chaotic coefficients
        for i in range(self.dim):
            nested = 0.0
            for k in range(1, 12):
                coeff = 0.4**k * (1.0 + 0.1 * np.sin(0.2 * k * i))
                nested += coeff * np.sin(2**(k) * x[i])
            result += nested
            
        # Penalty term with logarithmic scaling and chaotic multiplier
        penalty_mult = 1.1 + 0.3 * np.sin(0.1 * self.dim)  # Slightly increased multiplier
        result += penalty_mult * np.sum(np.log(np.abs(x) + 1.8))
        
        # Multi-modal component with exponential decay interactions and chaotic amplitude
        for i in range(self.dim):
            amp = 1.6 + 0.4 * np.sin(0.2 * i)  # Increased amplitude
            result += amp * np.exp(-0.6 * x[i]**2) * np.sin(5.0 * x[i])
            
        # Cross-dimensional polynomial coupling with dynamic coefficients and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.8 + 0.4 * np.sin(0.1 * (i + j) + 0.3 * np.cos(0.2 * i))  # Slightly increased coefficient
                result += coeff * (x[i]**3 + x[j]**3) * np.cos(x[i] * x[j])
                
        # Time-varying chaotic modulation with enhanced complexity
        for i in range(self.dim):
            mod1 = 1.3 + 0.2 * np.sin(0.3 * i)  # Slightly increased modulation
            mod2 = 1.1 + 0.1 * np.cos(0.4 * i)  # Slightly increased modulation
            result += mod1 * np.sin(np.pi * np.sin(mod2 * 4.0 * x[i])) * np.cos(np.pi * np.cos(mod2 * 3.0 * x[i]))
            
        # Additional high-frequency chaotic component
        for i in range(self.dim):
            result += 0.9 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.5 * x[i]**2)
            
        return result