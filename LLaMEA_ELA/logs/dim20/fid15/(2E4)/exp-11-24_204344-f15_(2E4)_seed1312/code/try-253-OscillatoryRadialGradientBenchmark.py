import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced radial basis function with chaotic scaling and multi-scale fractal structure
        rbf_term = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            # Multi-scale fractal radial component with chaotic modulation
            radial = np.exp(-0.05 * r**2) * (1.0 + 0.4 * np.sin(3.0 * r) + 0.2 * np.sin(9.0 * r) + 0.1 * np.sin(27.0 * r))
            rbf_term += radial
        
        # Chaotic sinusoidal oscillation with time-varying parameters and dynamic coupling
        sin_term = 0.0
        for i in range(self.dim):
            # Time-varying frequency and amplitude with chaotic modulation
            freq = 3.0 + 2.0 * np.sin(i * 0.4 + 1.5) + 0.5 * np.sin(11.0 * x[i])
            amp = 1.5 + 0.8 * np.cos(i * 0.2 + 0.7) + 0.3 * np.cos(13.0 * x[i])
            # Dynamic phase modulation
            phase_mod = 1.0 + 0.3 * np.sin(5.0 * x[i] + 2.0)
            sin_term += amp * np.sin(freq * phase_mod * x[i]) * np.cos(freq * phase_mod * x[i])
        
        # Asymmetric gradient field with dynamic scaling and recursive directional bias
        grad_term = 0.0
        for i in range(self.dim):
            # Dynamic bias with recursive position dependency
            bias = 1.0 + 0.6 * np.tanh(x[i] - 1.5) + 0.3 * np.sin(i * 0.8) + 0.2 * np.sin(7.0 * x[i])
            grad_term += bias * x[i]**4
        
        # Cross-dimensional recursive coupling with multi-scale interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale coupling with fractal-like behavior and recursive modulation
                coupling = np.sin(3.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j]))
                # Add multi-scale recursive modulation
                coupling *= (1.0 + 0.2 * np.sin(5.0 * (x[i] + x[j])) + 0.1 * np.sin(15.0 * (x[i] + x[j])))
                cross_term += coupling
        
        # Multi-modal wells with recursive structure, dynamic positions, and chaotic depth variations
        well_term = 0.0
        for i in range(self.dim):
            # Recursive well structure with varying depths and chaotic positioning
            well1 = (x[i] - 2.5)**2 * (x[i] + 2.5)**2
            well2 = (x[i] - 1.5)**4 + 0.7 * (x[i] + 1.5)**4
            # Chaotic depth modulation based on position and dimension
            depth_mod = 1.0 + 0.4 * np.sin(5.0 * x[i]) + 0.2 * np.cos(17.0 * x[i])
            well_term += 0.6 * well1 * depth_mod + 0.4 * well2 * depth_mod
        
        # Additional chaotic perturbation layer with recursive fractal structure
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.15 * np.sin(12.0 * x[i]) * np.cos(18.0 * x[i]) + 0.08 * np.sin(36.0 * x[i])
        
        # Final combination with adaptive weights and dynamic scaling
        total = 0.3 * rbf_term + 0.25 * sin_term + 0.2 * grad_term + 0.15 * cross_term + 0.1 * well_term + 0.05 * chaos_term
        
        # Global scaling with chaotic modulation and dimensionality adjustment
        scaling = 1.0 + 0.15 * self.dim + 0.08 * np.sin(self.dim * 0.4) + 0.06 * np.cos(self.dim * 0.8) + 0.03 * np.sin(self.dim * 2.0)
        
        return total * scaling