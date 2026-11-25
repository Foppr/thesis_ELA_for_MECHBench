import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal coupling weights with chaotic modulation
        self.fractal_weights = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1)) * 0.5 + 0.5
        # Dynamic polynomial exponents with chaotic variation
        self.exponents = 2.0 + 1.5 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical term with dynamic exponent
        f1 = np.sum(x**2)
        
        # Radial basis function component with chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            # Chaotic width modulation based on position and dimension
            width = 1.0 + 0.8 * np.sin(r / (self.dim + 1) + i / (self.dim + 3))
            f2 += np.exp(-0.5 * (x[i] / width)**2)
        
        # Sinusoidal grating component with fractal frequency scaling
        f3 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.8 * np.sin(i / (self.dim + 1) + np.cos(i * 0.7))
            f3 += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional coupling with fractal weights
        f4 = 0.0
        for i in range(self.dim - 1):
            weight = self.fractal_weights[i] * 0.8
            f4 += weight * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            
        # Nonlinear interaction with dynamic polynomial exponents
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.exp(-x[i]**2) * np.sin(3.0 * x[i]**self.exponents[i]) * np.cos(2.0 * x[i]**self.exponents[i])
        
        # Multimodal component with fractal-like structure
        f6 = 0.0
        for i in range(self.dim):
            f6 += (x[i]**4 - 10 * x[i]**2 + 8 * x[i]) * np.cos(x[i] * 0.5) * np.sin(x[i] * 0.3)
            
        # Chaotic coupling with time-varying phase and dynamic scaling
        f7 = 0.0
        for i in range(self.dim - 2):
            phase = np.sin(np.sum(x[:i+1])**2 / (self.dim + 2))
            scale = 1.0 + 0.5 * np.cos(i / (self.dim + 1))
            f7 += scale * np.sin(x[i] * x[i+1] + phase) * np.cos(x[i+2])
            
        # Fractal-like coupling with self-similar structure and dynamic scaling
        f8 = 0.0
        for i in range(self.dim - 3):
            scale = 0.7 + 0.3 * np.sin(i / (self.dim + 1))
            f8 += scale * np.sin(x[i] * x[i+1]) * np.cos(x[i+2] * x[i+3]) * np.sin(0.5 * x[i])
            
        # Sine-cosine coupled oscillations with adaptive coupling and chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.6 * np.sin(i / (self.dim + 2))
            f9 += (np.sin(x[i]) + np.cos(x[i])) * np.sin(x[i]**2) * mod
            
        # Combined scaling factor with chaotic variation
        scale_factor = 1.5 + 0.8 * np.sin(self.dim / 3.0)
        
        # Additional harmonic component with varying amplitudes and chaotic phases
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.5 * np.cos(i / (self.dim + 2) + np.sin(i * 0.6))
            phase = 0.5 + 0.3 * np.sin(i / (self.dim + 1) + np.cos(i * 0.4))
            f10 += amp * np.sin(2.0 * x[i] + phase) * np.cos(1.5 * x[i] + phase)
            
        # Saddle point structure with alternating signs and chaotic modulation
        f11 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.4 * np.sin(i / (self.dim + 1))
            if i % 2 == 0:
                f11 += x[i]**3 * mod
            else:
                f11 -= x[i]**3 * mod
                
        # Final combined function with chaotic scaling and fractal coupling
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)