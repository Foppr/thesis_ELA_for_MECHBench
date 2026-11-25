import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Base quadratic term with enhanced adaptive stiffness
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced adaptive stiffness with higher frequency components
            stiffness = 1.0 + 0.6 * np.sin(xi * 4.0) + 0.4 * np.cos(xi * 3.0) + 0.2 * np.sin(xi * 7.0)
            
            # Modified fractal basin boundary with stronger irregularity
            basin_mod = 1.0 + 0.5 * np.sin(8.0 * xi + self.dim * 0.6) + 0.3 * np.cos(5.0 * xi)
            
            # Enhanced chaotic resonance term with long-range coupling
            chaos_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    # Increased coupling strength and longer range
                    coupling = 0.2 * np.exp(-abs(i - j) * 0.3)
                    chaos_term += coupling * np.sin(xi + x_norm[j] * 1.5 + 0.4 * np.cos(i + j * 1.2))
            
            # Enhanced multi-modal component with stronger interference
            modal_component = xi**4 + 0.9 * np.sin(6.0 * xi) + 0.4 * np.cos(4.0 * xi) + 0.1 * np.sin(10.0 * xi)
            
            # Dynamic weighting with more complex modulation
            weight = 1.0 + 0.3 * np.sin(i * 0.6 + self.dim * 0.4)
            amplitude = 1.0 + 0.2 * np.cos(xi * 5.0 + i * 0.8) + 0.1 * np.sin(xi * 8.0)
            
            result += weight * amplitude * (stiffness * basin_mod * modal_component + 
                                          chaos_term**2)
        
        # Enhanced global scaling with stronger fractal dimension effect
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 3.0)
        
        # Improved chaotic attractor modulation with better conditioning
        attractor_mod = 1.0 + 0.3 * np.sin(np.sum(x_norm**3) * 2.0 + self.dim * 0.5)
        
        # Add additional conditioning term to improve fitness
        conditioning_term = 0.05 * np.sum(np.abs(x_norm)**1.5)
        
        # Final normalization and smoothing with improved scaling
        return (global_scale * attractor_mod * result / self.dim) + conditioning_term