import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic sine-wave modulation with dynamic frequency and amplitude
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.5 * np.cos(0.4 * i)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial basis function with dynamic centers and time-varying widths
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1))
            width = 0.5 + 0.3 * np.sin(0.2 * i)
            result += 2.0 * np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Polynomial chaos with dynamic exponents and chaotic coefficients
        for i in range(self.dim):
            exp = 3.0 + 2.0 * np.sin(0.1 * i)
            coeff = 1.5 + 0.8 * np.cos(0.2 * i)
            result += coeff * (x[i]**exp) * np.sin(0.5 * x[i])
            
        # Cross-dimensional coupling with chaotic phase shifts and variable interaction strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                phase = 0.2 * np.sin(0.3 * (i + j))
                strength = 1.0 + 0.5 * np.cos(0.1 * (i - j))
                result += strength * np.sin(x[i] + x[j] + phase) * np.cos(x[i] * x[j])
                
        # Multi-modal sine-polynomial component with dynamic frequency and amplitude
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.2 * i)
            amp = 1.2 + 0.8 * np.cos(0.3 * i)
            result += amp * np.sin(freq * x[i]) * (x[i]**4 - 2.0 * x[i]**2 + 1.0)
            
        # Hyperbolic tangent and cosine interactions with chaotic scaling
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.25 * i)
            result += scale * np.tanh(x[i]) * np.cos(2.0 * x[i])
            
        # Fractional power and chaotic logarithmic interactions
        for i in range(self.dim):
            exp = 1.5 + 0.4 * np.sin(0.3 * i)
            result += 0.8 * np.power(np.abs(x[i]), exp) * np.log(np.abs(x[i]) + 2.0)
            
        # Dynamic conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.2 * np.sin(0.1 * self.dim)
        result *= condition_factor
        
        # Nested chaotic sine components with recursive scaling
        for i in range(self.dim):
            nested_sum = 0.0
            for k in range(1, 8):
                scale = 0.3**k * (1.0 + 0.2 * np.sin(0.2 * k))
                nested_sum += scale * np.sin(2**(k) * x[i])
            result += nested_sum
            
        # Penalty term with chaotic coefficient and logarithmic scaling
        penalty_coeff = 0.7 + 0.3 * np.sin(0.4 * self.dim)
        result += penalty_coeff * np.sum(np.log(np.abs(x) + 1.5))
        
        return result