import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component with fractal-like recursive structure
        rbf_term = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            # Recursive radial component with fractal scaling
            radial = np.exp(-0.1 * r**2) * (1.0 + 0.3 * np.sin(5.0 * r) + 0.1 * np.sin(25.0 * r))
            rbf_term += radial
        
        # Sinusoidal oscillation component with dynamic frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5 + 1.0)
            amp = 1.0 + 0.5 * np.cos(i * 0.3 + 0.5)
            # Add chaotic modulation to frequencies
            freq_mod = 1.0 + 0.2 * np.sin(7.0 * x[i])
            sin_term += amp * np.sin(freq * freq_mod * x[i]) * np.cos(freq * freq_mod * x[i])
        
        # Asymmetric gradient field with directional bias and dynamic scaling
        grad_term = 0.0
        for i in range(self.dim):
            # Dynamic bias based on position and dimension
            bias = 1.0 + 0.5 * np.tanh(x[i] - 1.0) + 0.2 * np.sin(i * 0.7)
            grad_term += bias * x[i]**3
        
        # Cross-dimensional coupling with recursive interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive coupling with fractal-like behavior
                coupling = np.sin(2.0 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
                # Add recursive modulation
                coupling *= (1.0 + 0.1 * np.sin(3.0 * (x[i] + x[j])))
                cross_term += coupling
        
        # Multi-modal wells with recursive structure and dynamic positions
        well_term = 0.0
        for i in range(self.dim):
            # Recursive well structure with varying depths and positions
            well1 = (x[i] - 2.0)**2 * (x[i] + 2.0)**2
            well2 = (x[i] - 1.0)**4 + 0.5 * (x[i] + 1.0)**4
            # Add recursive modulation to well depths
            depth_mod = 1.0 + 0.3 * np.sin(4.0 * x[i])
            well_term += 0.5 * well1 * depth_mod + 0.3 * well2 * depth_mod
        
        # Additional chaotic perturbation layer
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.1 * np.sin(10.0 * x[i]) * np.cos(15.0 * x[i])
        
        # Final combination with adaptive weights and dynamic scaling
        total = 0.25 * rbf_term + 0.2 * sin_term + 0.18 * grad_term + 0.15 * cross_term + 0.12 * well_term + 0.08 * chaos_term
        
        # Global scaling and dimensionality adjustment with chaotic modulation
        scaling = 1.0 + 0.1 * self.dim + 0.05 * np.sin(self.dim * 0.3) + 0.03 * np.cos(self.dim * 0.7)
        
        return total * scaling