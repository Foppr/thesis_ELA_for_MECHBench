import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function with quaternion-inspired symmetry breaking
        rbf_term = 0.0
        centers = np.linspace(-4, 4, min(12, self.dim))
        for i in range(self.dim):
            dist = np.sum((x - centers[i % len(centers)])**2)
            # Add chaotic phase shift and adaptive decay
            phase_shift = np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            decay = 0.5 + 0.5 * np.sin(0.3 * i)
            rbf_term += np.exp(-decay * dist) * np.sin(2.0 * x[i] + phase_shift)
        
        # Sinusoidal oscillation with multi-fractal frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            # Fractal-like frequency modulation using golden ratio and chaotic maps
            freq = 1.0 + 0.7 * np.sin(1.618 * i + np.sin(3.14159 * x[i]))
            sin_term += np.sin(freq * x[i]) * np.cos(0.3 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with adaptive ridge structures
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited but adaptive coupling
                # Ridge structure with chaotic modulation
                ridge = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(3.0 * (x[i] - x[j]))
                coupling = (x[i] * x[j])**3 + np.sin(x[i] + x[j]) + ridge
                coupling_term += coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Adaptive polynomial with multi-scale chaotic modulation
        poly_term = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic modulation using multiple frequencies
            mod1 = 1.0 + 0.4 * np.sin(7.0 * x[i])
            mod2 = 1.0 + 0.3 * np.cos(5.0 * x[i])
            mod3 = 1.0 + 0.2 * np.sin(11.0 * x[i])
            poly_term += (mod1 * mod2 * mod3) * (x[i]**5 + 0.6 * x[i]**4 + 0.3 * x[i]**3 + 0.1 * x[i]**2 + 0.05 * x[i])
        
        # Fractal-like self-similarity with recursive structure and noise
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-fractal term with chaotic scaling
            scale = 1.0 + 0.3 * np.sin(2.0 * x[i])
            fractal_term += np.sin(scale * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Novel noise injection with multi-scale harmonics and chaotic phase
        noise = 0.0
        for k in range(1, 6):  # Multi-scale harmonics
            noise += (0.05 / k) * np.sin(k * 10.0 * x + k * np.sin(2.0 * x))
        
        # Add chaotic basin boundary interactions
        basin_term = 0.0
        for i in range(self.dim):
            # Create chaotic basins with non-smooth transitions
            basin_term += np.abs(np.sin(4.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Combine all terms with proper scaling and chaos amplification
        return 1.2 * rbf_term + 0.8 * sin_term + 0.6 * coupling_term + 0.5 * poly_term + 0.3 * fractal_term + noise + 0.2 * basin_term + 0.01 * np.sum(x**2)