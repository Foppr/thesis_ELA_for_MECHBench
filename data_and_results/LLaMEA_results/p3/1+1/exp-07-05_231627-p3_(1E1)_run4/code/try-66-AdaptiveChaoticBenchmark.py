import numpy as np

class AdaptiveChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for consistent scaling
        x_norm = x / 5.0
        
        # Base quadratic component with adaptive weights
        base = np.sum(x_norm**2)
        
        # Chaotic sine modulation with position-dependent frequency
        freq_mod = 10 + 5 * np.sin(2 * np.pi * np.sum(x_norm**2))
        chaotic = np.sum(np.sin(freq_mod * x_norm) * np.cos(freq_mod * x_norm**2))
        
        # Dynamic polynomial with varying exponents based on position
        poly = 0
        for i in range(self.dim):
            exp = 3 + 2 * np.sin(x_norm[i] * np.pi)
            poly += x_norm[i]**exp
        
        # Saddle point structure with varying depth
        saddle = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle += (x_norm[i]**2 - x_norm[i+1]**2)**2
        
        # Adaptive Gaussian peaks with dynamic centers and widths
        peaks = 0
        num_peaks = min(20, self.dim * 2)
        for i in range(num_peaks):
            center = np.sin(i * np.pi / num_peaks) * np.ones(self.dim)
            width = 0.5 + 0.5 * np.cos(i * np.pi / num_peaks)
            peaks += np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Cross-dimensional interaction with position-dependent coupling
        interaction = 0
        for i in range(self.dim - 1):
            coupling = 0.5 + 0.5 * np.sin(x_norm[i] * np.pi)
            interaction += coupling * (x_norm[i] - x_norm[i+1])**4
        
        # Fractional curvature component
        frac_curvature = np.sum(np.abs(x_norm)**1.7)
        
        # Combine components with dynamic weights
        weights = np.array([0.3, 0.25, 0.2, 0.15, 0.05, 0.05])
        components = np.array([base, chaotic, poly, saddle, interaction, frac_curvature])
        
        result = np.dot(weights, components)
        
        # Add position-dependent noise
        noise = 0.02 * np.abs(np.sum(x_norm**3)) * np.random.uniform(-1, 1)
        
        return result + noise