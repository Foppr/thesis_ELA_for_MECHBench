import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 0.35
        self.saddle_strength = 2.8
        self.coupling_strength = 2.1
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial term with non-integer exponents
        fractal_term = np.sum(np.abs(x)**(2.7 + self.fractal_dim * np.sin(x[0] if len(x) > 0 else 0))) * 0.12
        
        # Asymmetric saddle points with varying heights and widths
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create asymmetric saddle with different curvature on each side
            if xi >= 0:
                saddle_term += self.saddle_strength * (xi**4 - 2*xi**2) * np.exp(-0.12 * xi**2)
            else:
                saddle_term += self.saddle_strength * (xi**3 - xi) * np.exp(-0.06 * xi**2)
        
        # Dynamic coupling between dimensions with phase shifts
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling with varying strength and phase
                phase = np.sin(0.6 * (i + j))
                coupling_term += self.coupling_strength * np.sin(x[i] + x[j] + phase) * \
                                (x[i]**2 + x[j]**2) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        mod_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components with different amplitudes
            mod_term += (np.sin(xi * 3.5) * np.cos(xi * 1.9) * np.exp(-0.22 * xi**2) + 
                        np.sin(xi * 5.5) * np.cos(xi * 3.1) * np.exp(-0.12 * xi**2) +
                        np.sin(xi * 7.7) * np.cos(xi * 4.3) * np.exp(-0.06 * xi**2))
        
        # Asymmetric radial component with dynamic conditioning
        radial_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Radial term with asymmetric behavior based on sign of dimension
            if xi >= 0:
                radial_term += (xi**3 + 0.5*xi**2) * np.exp(-0.17 * xi**2)
            else:
                radial_term += (xi**4 - 0.3*xi**3) * np.exp(-0.12 * xi**2)
        
        # Combine all terms with proper scaling
        return 0.5 * fractal_term + 1.2 * saddle_term + 0.8 * coupling_term + 0.6 * mod_term + 0.4 * radial_term