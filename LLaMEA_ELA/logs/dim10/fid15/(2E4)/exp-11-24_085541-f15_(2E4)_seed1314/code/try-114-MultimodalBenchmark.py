import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic cubic spline component with memory effect
        for i in range(self.dim):
            spline_val = 0.0
            for k in range(1, 6):
                freq = 2.0 * k + 0.5 * np.sin(0.3 * i * k)
                amp = 1.0 + 0.3 * np.cos(0.4 * i * k)
                spline_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            result += 0.5 * spline_val
            
        # Memory-dependent conditioning with chaotic scaling
        if self.dim > 1:
            memory_term = 0.0
            for i in range(self.dim - 1):
                memory_term += (x[i] * x[i+1]) * np.sin(0.5 * (i + 1) * np.pi)
            result += 0.3 * memory_term
            
        # Fractal-like dimension coupling with recursive interaction
        for i in range(self.dim):
            fractal_interaction = 0.0
            for j in range(1, min(5, self.dim)):
                coeff = 0.8 + 0.2 * np.sin(0.2 * (i + j))
                fractal_interaction += coeff * np.sin(3.0 * x[i] + 0.5 * x[j])
            result += 0.4 * fractal_interaction
            
        # Dynamic phase-shifted polynomial interactions
        for i in range(self.dim):
            phase = 0.2 * np.sin(0.3 * i) + 0.1 * np.cos(0.4 * i)
            poly_val = x[i]**5 + 0.7 * x[i]**4 + 0.5 * x[i]**3 + 0.3 * x[i]**2 + 0.1 * x[i]
            result += 1.5 * np.sin(poly_val + phase)
            
        # Cross-dimensional chaotic coupling with exponential decay
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                coeff = 1.2 + 0.3 * np.sin(0.2 * (i + j))
                coupling_sum += coeff * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2.0 * x[i] * x[j])
            result += 0.8 * coupling_sum
            
        # Hyperbolic tangent component with dynamic coefficients
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(0.4 * i)
            result += coeff * np.tanh(2.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Adaptive chaotic scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(0.3 * self.dim) + 0.1 * np.cos(0.2 * self.dim)
        result *= scale_factor
        
        # Multi-modal exponential interactions with dynamic amplitudes
        for i in range(self.dim):
            amp = 1.5 + 0.4 * np.sin(0.3 * i)
            result += amp * np.exp(-0.3 * x[i]**2) * np.cos(4.0 * x[i])
            
        # Memory-dependent chaotic modulation with temporal correlation
        if self.dim > 2:
            corr_term = 1.0 + 0.2 * np.sin(0.5 * (x[0] - x[-1]))
            result *= corr_term
            
        return result