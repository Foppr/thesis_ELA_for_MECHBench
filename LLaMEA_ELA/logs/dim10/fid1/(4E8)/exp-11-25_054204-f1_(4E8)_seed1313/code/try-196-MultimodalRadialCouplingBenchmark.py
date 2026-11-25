import numpy as np

class MultimodalRadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for dynamic coupling
        self.radial_weights = np.exp(-np.arange(1, dim + 1) / (dim / 2.0))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Radial basis function component with dynamic scaling
        f2 = 0.0
        for i in range(self.dim):
            # Radial distance from origin
            r = np.sqrt(np.sum(x**2))
            # Dynamic radial basis with varying width
            width = 1.0 + 0.5 * np.sin(r / 2.0)
            f2 += np.exp(-0.5 * (x[i] / width)**2)
        
        # Sinusoidal grating component with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i / (self.dim + 1))
            f3 += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional coupling with radial weights
        f4 = 0.0
        for i in range(self.dim - 1):
            weight = self.radial_weights[i]
            f4 += weight * np.sin(x[i] * x[i+1])
            
        # Nonlinear interaction with exponential modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.exp(-x[i]**2) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Multimodal component with multiple local minima
        f6 = 0.0
        for i in range(self.dim):
            f6 += (x[i]**4 - 10 * x[i]**2 + 5 * x[i]) * np.cos(x[i])
            
        # Dynamic coupling with time-varying phase
        f7 = 0.0
        for i in range(self.dim - 2):
            phase = np.sin(np.sum(x[:i+1])**2 / 10.0)
            f7 += np.sin(x[i] * x[i+1] + phase) * np.cos(x[i+2])
            
        # Fractal-like coupling with self-similar structure
        f8 = 0.0
        for i in range(self.dim - 3):
            f8 += np.sin(x[i] * x[i+1]) * np.cos(x[i+2] * x[i+3]) * np.sin(0.5 * x[i])
            
        # Sine-cosine coupled oscillations with adaptive coupling
        f9 = 0.0
        for i in range(self.dim):
            f9 += (np.sin(x[i]) + np.cos(x[i])) * np.sin(x[i]**2)
            
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Additional harmonic component with varying amplitudes
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.cos(i / (self.dim + 1))
            f10 += amp * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            
        # Saddle point structure with alternating signs
        f11 = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                f11 += x[i]**3
            else:
                f11 -= x[i]**3
                
        # Final combined function
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)