import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 0.5
        self.saddle_strength = 3.0
        self.coupling_strength = 2.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial term with non-integer exponents and chaotic modulation
        fractal_term = np.sum(np.abs(x)**(3.1 + self.fractal_dim * np.sin(x[0] if len(x) > 0 else 0) + 
                                         0.3 * np.cos(x[1] if len(x) > 1 else 0))) * 0.15
        
        # Asymmetric saddle points with varying heights, widths and chaotic curvature
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create asymmetric saddle with different curvature on each side and chaotic modulation
            if xi >= 0:
                saddle_term += self.saddle_strength * (xi**5 - 3*xi**3 + xi) * np.exp(-0.12 * xi**2)
            else:
                saddle_term += self.saddle_strength * (xi**4 - 2*xi**2) * np.exp(-0.08 * xi**2)
        
        # Dynamic coupling between dimensions with chaotic phase shifts and stronger interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling with varying strength, phase and chaotic modulation
                phase = np.sin(0.7 * (i + j) + 0.5 * np.cos(i * j))
                coupling_term += self.coupling_strength * np.sin(x[i] + x[j] + phase) * \
                                (x[i]**2 + x[j]**2 + 0.5 * np.sin(x[i] * x[j])) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Multi-scale sinusoidal modulation with higher frequencies and chaotic amplitudes
        mod_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple high-frequency components with chaotic amplitudes
            mod_term += (np.sin(xi * 4.5) * np.cos(xi * 2.1) * np.exp(-0.25 * xi**2) + 
                        np.sin(xi * 6.8) * np.cos(xi * 3.7) * np.exp(-0.15 * xi**2) +
                        np.sin(xi * 9.2) * np.cos(xi * 5.4) * np.exp(-0.1 * xi**2) +
                        np.sin(xi * 11.7) * np.cos(xi * 7.3) * np.exp(-0.08 * xi**2))
        
        # Asymmetric radial component with dynamic conditioning and chaotic behavior
        radial_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Radial term with asymmetric behavior and chaotic modulation based on sign of dimension
            if xi >= 0:
                radial_term += (xi**4 + 0.7*xi**3 - 0.2*xi**2) * np.exp(-0.2 * xi**2)
            else:
                radial_term += (xi**5 - 0.4*xi**4 + 0.1*xi**3) * np.exp(-0.15 * xi**2)
        
        # Combine all terms with proper scaling
        return 0.6 * fractal_term + 1.5 * saddle_term + 1.0 * coupling_term + 0.7 * mod_term + 0.5 * radial_term