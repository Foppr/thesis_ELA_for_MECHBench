import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic saddle component with fractal-like bifurcation zones
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create fractal-like asymmetric bifurcation zones
            if xi < -0.4:
                saddle += 2.5 * np.sin(18.0 * xi) * np.exp(-0.6 * xi**2)
            elif xi > 0.4:
                saddle += 2.0 * np.cos(15.0 * xi) * np.exp(-0.4 * xi**2)
            else:
                # Enhanced central chaotic region with fractal self-similarity
                saddle += 1.2 * np.sin(25.0 * xi + 0.7 * np.sin(35.0 * xi)) * np.exp(-0.8 * xi**2)
        
        # Adaptive basin boundary component with quantum-inspired curvature
        basins = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like sigmoidal transitions with adaptive parameters
            boundary = 1.0 / (1.0 + np.exp(-12.0 * (xi - 0.15)))
            curvature = 2.5 + 2.0 * np.sin(10.0 * xi)
            basins += curvature * boundary * (xi**4 - 2.5 * xi**2 + 0.8)
        
        # Multi-scale harmonic interference with quantum coupling
        harmonics = 0.0
        freq_mod = 1.2 + 0.4 * np.sin(0.6 * self.dim)
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-inspired harmonic components at different scales
            scale_factor = 2.5**(i % 5)
            harmonics += (0.6 + 0.4 * np.sin(scale_factor * xi)) * \
                        np.cos(freq_mod * scale_factor * xi) * \
                        np.exp(-0.3 * xi**2)
        
        # Cross-dimensional coupling with quantum-inspired interaction coefficients
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Quantum-inspired coupling strength based on dimension index
                asym_strength = 0.9 + 0.3 * np.sin(0.4 * (i - j))
                dist = np.sqrt((xi - xj)**2 + 0.15)
                cross += asym_strength * np.sin(18.0 * dist) * np.exp(-dist**2)
        
        # Quantum-inspired time-varying landscape modulation
        time_mod = 1.0 + 0.5 * np.sin(0.3 * self.dim + np.sum(x_norm))
        landscape_mod = 0.6 * np.cos(4.0 * np.sum(x_norm)) + 0.4 * np.sin(6.0 * np.sum(x_norm))
        
        # Combine all components with optimized weights
        weight_saddle = 0.5 + 0.15 * np.sin(self.dim * 0.35)
        weight_basins = 0.25 + 0.1 * np.cos(self.dim * 0.25)
        weight_harmonics = 0.2 + 0.2 * np.tanh(self.dim * 0.15)
        weight_cross = 0.3
        
        return time_mod * (weight_saddle * saddle + 
                          weight_basins * basins + 
                          weight_harmonics * harmonics + 
                          weight_cross * cross) + landscape_mod