import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic cubic spline component with modified memory effect
        for i in range(self.dim):
            spline_val = 0.0
            for k in range(1, 7):
                freq = 3.0 * k + 0.5 * np.sin(0.4 * i * k)
                amp = 1.3 + 0.3 * np.cos(0.5 * i * k)
                spline_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            result += 0.7 * spline_val
            
        # Memory-dependent conditioning with modified scaling
        if self.dim > 1:
            memory_term = 0.0
            for i in range(self.dim - 1):
                memory_term += (x[i] * x[i+1]) * np.sin(0.7 * (i + 1) * np.pi)
            result += 0.5 * memory_term
            
        # Fractal-like dimension coupling with altered interaction
        for i in range(self.dim):
            fractal_interaction = 0.0
            for j in range(1, min(6, self.dim)):
                coeff = 1.0 + 0.2 * np.sin(0.3 * (i + j))
                fractal_interaction += coeff * np.sin(4.0 * x[i] + 0.7 * x[j])
            result += 0.4 * fractal_interaction
            
        # Dynamic phase-shifted polynomial interactions with modified exponents
        for i in range(self.dim):
            phase = 0.3 * np.sin(0.4 * i) + 0.2 * np.cos(0.5 * i)
            poly_val = x[i]**7 + 0.9 * x[i]**6 + 0.7 * x[i]**5 + 0.5 * x[i]**4 + 0.3 * x[i]**3 + 0.15 * x[i]**2 + 0.05 * x[i]
            result += 2.0 * np.sin(poly_val + phase)
            
        # Cross-dimensional chaotic coupling with modified decay
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                coeff = 1.4 + 0.3 * np.sin(0.3 * (i + j))
                coupling_sum += coeff * np.exp(-0.7 * (x[i] - x[j])**2) * np.sin(3.0 * x[i] * x[j])
            result += 1.0 * coupling_sum
            
        # Hyperbolic tangent component with modified coefficients
        for i in range(self.dim):
            coeff = 1.2 + 0.5 * np.sin(0.5 * i)
            result += coeff * np.tanh(3.0 * x[i]) * np.cos(4.0 * x[i])
            
        # Adaptive chaotic scaling with modified factors
        scale_factor = 1.2 + 0.2 * np.sin(0.4 * self.dim) + 0.15 * np.cos(0.3 * self.dim)
        result *= scale_factor
        
        # Multi-modal exponential interactions with adjusted amplitudes
        for i in range(self.dim):
            amp = 1.8 + 0.4 * np.sin(0.4 * i)
            result += amp * np.exp(-0.4 * x[i]**2) * np.cos(5.0 * x[i])
            
        # Memory-dependent chaotic modulation with modified correlation
        if self.dim > 2:
            corr_term = 1.2 + 0.2 * np.sin(0.6 * (x[0] - x[-1]))
            result *= corr_term
            
        return result