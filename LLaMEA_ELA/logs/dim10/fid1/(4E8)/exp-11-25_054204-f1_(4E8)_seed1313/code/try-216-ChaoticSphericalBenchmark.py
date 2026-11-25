import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal coupling weights with chaotic modulation
        self.fractal_weights = np.sin(np.arange(1, dim + 1) * np.pi / (dim * 2.0)) * 0.5 + 0.5
        # Dynamic polynomial exponents with chaotic variation
        self.exponents = 2.0 + 1.5 * np.sin(np.arange(dim) * np.pi / (dim * 1.3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical term with dynamic exponent
        f1 = np.sum(x**2)
        
        # Radial basis function component with chaotic modulation
        f2 = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            width = 1.0 + 0.8 * np.sin(r / 2.5 + i / (self.dim + 1))
            f2 += np.exp(-0.5 * (x[i] / width)**2) * np.cos(0.5 * r)
        
        # Sinusoidal grating with chaotic frequency modulation
        f3 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i / (self.dim + 1) + np.cos(x[i]))
            f3 += np.sin(freq * x[i]) * np.cos(freq * x[i] + np.sin(x[i]))
        
        # Cross-dimensional coupling with fractal weights and chaotic phase
        f4 = 0.0
        for i in range(self.dim - 1):
            weight = self.fractal_weights[i] * (0.8 + 0.4 * np.sin(i / (self.dim + 1)))
            phase = np.sin(x[i] * x[i+1] * 0.5)
            f4 += weight * np.sin(x[i] * x[i+1] + phase) * np.cos(x[i]**2 + x[i+1]**2)
            
        # Nonlinear interaction with dynamic polynomial exponents
        f5 = 0.0
        for i in range(self.dim):
            f5 += (x[i]**self.exponents[i]) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Multimodal component with fractal-like structure and chaotic modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += (x[i]**4 - 10 * x[i]**2 + 5 * x[i]) * np.cos(x[i] * 0.7) * np.sin(0.3 * x[i])
            
        # Dynamic coupling with time-varying chaotic phase
        f7 = 0.0
        for i in range(self.dim - 2):
            phase = np.sin(np.sum(x[:i+1])**2 / 6.0 + i / (self.dim + 1))
            f7 += np.sin(x[i] * x[i+1] + phase) * np.cos(x[i+2] * 0.8)
            
        # Fractal-like coupling with self-similar structure and chaotic scaling
        f8 = 0.0
        for i in range(self.dim - 3):
            scale = 0.5 + 0.5 * np.sin(i / (self.dim + 1) + np.cos(x[i]))
            f8 += scale * np.sin(x[i] * x[i+1]) * np.cos(x[i+2] * x[i+3]) * np.sin(0.6 * x[i])
            
        # Sine-cosine coupled oscillations with adaptive coupling and chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            f9 += (np.sin(x[i]) + np.cos(x[i])) * np.sin(x[i]**2 + 0.5 * np.sin(i))
            
        # Combined scaling factor based on dimensionality with chaotic variation
        scale_factor = 1.0 + 0.8 * np.log(self.dim + 1) * np.sin(self.dim / 3.0)
        
        # Additional harmonic component with chaotic amplitude modulation
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(i / (self.dim + 1) + np.cos(x[i]))
            f10 += amp * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i] + np.sin(x[i]))
            
        # Saddle point structure with alternating signs and chaotic modulation
        f11 = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                f11 += x[i]**3
            elif i % 3 == 1:
                f11 -= x[i]**3 * np.sin(x[i])
            else:
                f11 += x[i]**3 * np.cos(x[i])
                
        # Final combined function with chaotic scaling and fractal structure
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)