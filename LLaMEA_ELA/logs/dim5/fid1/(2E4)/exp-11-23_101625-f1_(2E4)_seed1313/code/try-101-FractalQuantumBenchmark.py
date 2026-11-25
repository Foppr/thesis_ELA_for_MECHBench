import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Fractal-like ridge structures with self-similar patterns
        for i in range(self.dim):
            # Multi-scale fractal ridges with varying amplitudes
            ridge_sum = 0.0
            for k in range(1, 6):
                scale = 2**k
                amplitude = 1.0 / (k * (k + 1))
                ridge_sum += amplitude * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.5)
            result += 1.5 * ridge_sum
            
        # Quantum tunneling effects with probabilistic potential wells
        for i in range(self.dim):
            # Create dynamic energy wells with quantum-like interference
            well_depth = 2.0 + 1.2 * np.sin(i * 0.7 + np.sum(x) * 0.3)
            tunnel_prob = 0.5 * (1 + np.tanh(0.5 * x[i]))
            result += well_depth * tunnel_prob * np.exp(-0.5 * (x[i] - 2.0 * np.sin(i * 0.4))**2)
            
        # Dynamic energy wells with time-varying positions and depths
        for i in range(self.dim):
            # Wells that shift based on global position
            well_pos = 3.0 * np.cos(i * 0.5 + np.sum(x) * 0.2)
            well_depth = 1.8 + 0.8 * np.sin(i * 0.6 + np.sum(x) * 0.4)
            result += well_depth * np.exp(-0.5 * (x[i] - well_pos)**2)
            
        # Cross-dimensional quantum interference terms
        for i in range(self.dim):
            interference = 0.0
            for j in range(min(i+4, self.dim)):
                if i != j:
                    coupling_strength = 1.0 + 0.5 * np.sin(i * j * 0.3 + np.sum(x) * 0.2)
                    interference += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
            result += 0.7 * interference
            
        # Fractal harmonic modulation with multi-scale frequencies
        for i in range(self.dim):
            freq_sum = 0.0
            for k in range(1, 5):
                freq = 2**(k) * (1 + 0.3 * np.sin(i * k * 0.4))
                freq_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            result += 0.8 * freq_sum
            
        # Asymmetric barrier potentials with quantum-like tunneling
        for i in range(self.dim):
            # Create asymmetric barriers with exponential scaling
            barrier_left = 2.5 * np.exp(-0.5 * (x[i] + 3.0)**2) * (1 + 0.3 * np.sin(x[i]))
            barrier_right = 2.5 * np.exp(-0.5 * (x[i] - 3.0)**2) * (1 + 0.3 * np.cos(x[i]))
            result += barrier_left + barrier_right
            
        # Radial quantum harmonic interference
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            radial_freq = 4.0 + 2.0 * np.sin(r * 0.2)
            result += 1.3 * np.sin(radial_freq * r) * np.cos(radial_freq * r * 0.5)
            
        # Multi-scale fractal basin interactions
        basin_sum = 0.0
        for k in range(1, 4):
            scale = 2**k
            for i in range(self.dim):
                basin_sum += (1.0 / scale) * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.3)
        result += 0.9 * basin_sum
        
        return result