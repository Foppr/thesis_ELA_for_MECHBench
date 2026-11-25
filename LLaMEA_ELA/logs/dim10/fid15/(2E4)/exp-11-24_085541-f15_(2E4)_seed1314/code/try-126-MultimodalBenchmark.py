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
            for k in range(1, 10):
                freq = 4.0 * k + 0.8 * np.sin(0.5 * i * k)
                amp = 2.0 + 0.5 * np.cos(0.6 * i * k)
                spline_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            result += 1.0 * spline_val
            
        # Memory-dependent conditioning with chaotic scaling
        if self.dim > 1:
            memory_term = 0.0
            for i in range(self.dim - 1):
                memory_term += (x[i] * x[i+1]) * np.sin(0.8 * (i + 1) * np.pi)
            result += 0.7 * memory_term
            
        # Fractal-like dimension coupling with recursive interaction
        for i in range(self.dim):
            fractal_interaction = 0.0
            for j in range(1, min(9, self.dim)):
                coeff = 1.2 + 0.4 * np.sin(0.4 * (i + j))
                fractal_interaction += coeff * np.sin(5.0 * x[i] + 0.7 * x[j])
            result += 0.8 * fractal_interaction
            
        # Dynamic phase-shifted polynomial interactions
        for i in range(self.dim):
            phase = 0.4 * np.sin(0.5 * i) + 0.3 * np.cos(0.6 * i)
            poly_val = x[i]**9 + 0.9 * x[i]**8 + 0.7 * x[i]**7 + 0.5 * x[i]**6 + 0.3 * x[i]**5 + 0.15 * x[i]**4 + 0.08 * x[i]**3 + 0.04 * x[i]**2 + 0.02 * x[i]
            result += 2.5 * np.sin(poly_val + phase)
            
        # Cross-dimensional chaotic coupling with exponential decay
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+6, self.dim)):
                coeff = 2.0 + 0.5 * np.sin(0.4 * (i + j))
                coupling_sum += coeff * np.exp(-0.8 * (x[i] - x[j])**2) * np.sin(4.0 * x[i] * x[j])
            result += 1.5 * coupling_sum
            
        # Hyperbolic tangent component with dynamic coefficients
        for i in range(self.dim):
            coeff = 2.0 + 0.7 * np.sin(0.6 * i)
            result += coeff * np.tanh(4.0 * x[i]) * np.cos(5.0 * x[i])
            
        # Adaptive chaotic scaling based on dimensionality
        scale_factor = 1.5 + 0.4 * np.sin(0.5 * self.dim) + 0.3 * np.cos(0.4 * self.dim)
        result *= scale_factor
        
        # Multi-modal exponential interactions with dynamic amplitudes
        for i in range(self.dim):
            amp = 2.5 + 0.6 * np.sin(0.5 * i)
            result += amp * np.exp(-0.5 * x[i]**2) * np.cos(6.0 * x[i])
            
        # Memory-dependent chaotic modulation with temporal correlation
        if self.dim > 2:
            corr_term = 1.5 + 0.4 * np.sin(0.7 * (x[0] - x[-1]))
            result *= corr_term
            
        # Additional high-frequency chaotic modulation
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.7 * i)
            result += freq_mod * np.sin(12.0 * x[i]) * np.cos(12.0 * x[i])
            
        # Enhanced cross-dimensional coupling with dynamic weights
        for i in range(self.dim):
            enhanced_coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 2.5 + 0.6 * np.sin(0.4 * (i + j))
                    enhanced_coupling += weight * np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(2.0 * x[i] + 2.0 * x[j])
            result += 0.9 * enhanced_coupling
            
        # Add a new hyperbolic sine component with dynamic coefficients
        for i in range(self.dim):
            coeff = 1.8 + 0.6 * np.sin(0.5 * i)
            result += coeff * np.sinh(2.5 * x[i]) * np.cos(3.5 * x[i])
            
        # Add a new fractal dimension coupling with recursive interaction
        for i in range(self.dim):
            fractal_interaction = 0.0
            for j in range(1, min(8, self.dim)):
                coeff = 1.3 + 0.3 * np.sin(0.4 * (i + j))
                fractal_interaction += coeff * np.cos(6.0 * x[i] + 0.5 * x[j])
            result += 0.7 * fractal_interaction
            
        return result