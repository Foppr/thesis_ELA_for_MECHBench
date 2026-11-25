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
            
        # Radial basis function with dynamic centers, widths, and chaotic amplitude modulation
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                amplitude1 = 2.5 + 0.5 * np.sin(0.3 * i)
                amplitude2 = 1.8 + 0.3 * np.cos(0.4 * i)
                result += amplitude1 * np.exp(-0.4 * (x[i] - centers[i])**2) + amplitude2 * np.exp(-0.2 * (x[i] + centers[i])**2)
                
        # Dynamic cross-dimensional coupling with time-varying sinusoids and chaotic frequency modulation
        t = 1.5 + 0.2 * self.dim + 0.1 * np.sin(0.5 * self.dim)  # Time parameter with chaos
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                freq_mod = 1.0 + 0.3 * np.cos(0.2 * (i + j))
                coupling = np.sin(freq_mod * t * x[i] * x[j]) * np.cos(0.6 * t * (x[i]**2 + x[j]**2))
                result += 2.0 * coupling
                
        # Multi-modal sine-polynomial interactions with chaotic phase shifts
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.4 * i)
            result += 3.0 * np.sin(3.0 * x[i] + phase_shift) * (x[i]**5 - 2.5 * x[i]**3 + 1.5 * x[i])
            
        # Fractional power chaotic component with dynamic exponent
        for i in range(self.dim):
            exponent = 1.8 + 0.2 * np.sin(0.3 * i)
            result += 2.0 * np.power(np.abs(x[i]), exponent) * np.sin(6.0 * x[i])
            
        # Adaptive conditioning based on dimensionality with chaotic scaling
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.1 * np.cos(0.2 * self.dim)
        result *= condition_factor
        
        # Complex hyperbolic interactions with dynamic coefficients
        for i in range(self.dim):
            coeff1 = 1.5 + 0.3 * np.sin(0.2 * i)
            coeff2 = 1.0 + 0.2 * np.cos(0.3 * i)
            result += coeff1 * np.sinh(1.8 * x[i]) * np.cos(2.5 * x[i]) + coeff2 * np.cosh(1.5 * x[i]) * np.sin(2.2 * x[i])
            
        # Nested trigonometric component with recursive structure and chaotic scaling
        for i in range(self.dim):
            nested = 0.0
            for k in range(1, 12):
                scale = 0.4**k * (1.0 + 0.1 * np.sin(0.3 * k))
                nested += scale * np.sin(2**(k) * x[i])
            result += nested
            
        # Penalty term with logarithmic scaling and chaotic coefficient
        penalty_coeff = 0.8 + 0.2 * np.sin(0.5 * self.dim)
        result += penalty_coeff * np.sum(np.log(np.abs(x) + 1.8))
        
        # Multi-modal component with exponential decay interactions and dynamic amplitude
        for i in range(self.dim):
            amp = 1.2 + 0.3 * np.cos(0.4 * i)
            result += amp * np.exp(-0.6 * x[i]**2) * np.sin(5.0 * x[i])
            
        # Cross-dimensional polynomial coupling with dynamic coefficients and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.7 + 0.4 * np.sin(0.1 * (i + j)) * np.cos(0.2 * (i - j))
                result += coeff * (x[i]**3 + x[j]**3) * np.cos(x[i] * x[j])
                
        # Time-varying chaotic modulation with multiple frequency components
        for i in range(self.dim):
            freq1 = 4.5 + 0.5 * np.sin(0.3 * i)
            freq2 = 3.5 + 0.4 * np.cos(0.4 * i)
            result += 1.2 * np.sin(np.pi * np.sin(freq1 * x[i])) * np.cos(np.pi * np.cos(freq2 * x[i]))
            
        return result