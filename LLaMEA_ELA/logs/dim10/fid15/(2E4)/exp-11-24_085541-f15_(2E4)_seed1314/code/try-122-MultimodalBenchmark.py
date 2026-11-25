import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic cubic spline component with modified memory effect
        for i in range(self.dim):
            spline_val = 0.0
            for k in range(1, 6):
                freq = 2.5 * k + 0.4 * np.sin(0.35 * i * k)
                amp = 1.2 + 0.25 * np.cos(0.45 * i * k)
                spline_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            result += 0.6 * spline_val
            
        # Memory-dependent conditioning with modified scaling
        if self.dim > 1:
            memory_term = 0.0
            for i in range(self.dim - 1):
                memory_term += (x[i] * x[i+1]) * np.sin(0.6 * (i + 1) * np.pi)
            result += 0.4 * memory_term
            
        # Fractal-like dimension coupling with altered interaction
        for i in range(self.dim):
            fractal_interaction = 0.0
            for j in range(1, min(5, self.dim)):
                coeff = 0.9 + 0.15 * np.sin(0.25 * (i + j))
                fractal_interaction += coeff * np.sin(3.5 * x[i] + 0.6 * x[j])
            result += 0.3 * fractal_interaction
            
        # Dynamic phase-shifted polynomial interactions with modified exponents
        for i in range(self.dim):
            phase = 0.25 * np.sin(0.35 * i) + 0.15 * np.cos(0.45 * i)
            poly_val = x[i]**6 + 0.8 * x[i]**5 + 0.6 * x[i]**4 + 0.4 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i]
            result += 1.7 * np.sin(poly_val + phase)
            
        # Cross-dimensional chaotic coupling with modified decay
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+4, self.dim)):
                coeff = 1.3 + 0.25 * np.sin(0.25 * (i + j))
                coupling_sum += coeff * np.exp(-0.6 * (x[i] - x[j])**2) * np.sin(2.5 * x[i] * x[j])
            result += 0.9 * coupling_sum
            
        # Hyperbolic tangent component with modified coefficients
        for i in range(self.dim):
            coeff = 1.1 + 0.4 * np.sin(0.45 * i)
            result += coeff * np.tanh(2.5 * x[i]) * np.cos(3.5 * x[i])
            
        # Adaptive chaotic scaling with modified factors
        scale_factor = 1.1 + 0.15 * np.sin(0.35 * self.dim) + 0.12 * np.cos(0.25 * self.dim)
        result *= scale_factor
        
        # Multi-modal exponential interactions with adjusted amplitudes
        for i in range(self.dim):
            amp = 1.6 + 0.35 * np.sin(0.35 * i)
            result += amp * np.exp(-0.35 * x[i]**2) * np.cos(4.5 * x[i])
            
        # Memory-dependent chaotic modulation with modified correlation
        if self.dim > 2:
            corr_term = 1.1 + 0.18 * np.sin(0.55 * (x[0] - x[-1]))
            result *= corr_term
            
        return result