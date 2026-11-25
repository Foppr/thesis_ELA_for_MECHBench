import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic saddle with quantum-inspired interference patterns
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like bifurcation zones with phase modulation
            if xi < -0.3:
                saddle += 3.2 * np.sin(22.0 * xi + 0.5 * np.sin(42.0 * xi)) * np.exp(-0.5 * xi**2)
            elif xi > 0.3:
                saddle += 2.1 * np.cos(18.0 * xi + 0.3 * np.cos(30.0 * xi)) * np.exp(-0.3 * xi**2)
            else:
                # Ultra-fractal central region with nested chaotic patterns
                saddle += 1.5 * np.sin(35.0 * xi + 0.8 * np.sin(50.0 * xi) + 0.4 * np.sin(70.0 * xi)) * np.exp(-0.7 * xi**2)
        
        # Dynamic basin boundary with quantum tunneling probabilities
        basins = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like sigmoidal transitions with probabilistic curvature
            boundary = 1.0 / (1.0 + np.exp(-15.0 * (xi - 0.2)))
            curvature = 3.0 + 1.5 * np.sin(12.0 * xi + 0.6 * np.cos(20.0 * xi))
            basins += curvature * boundary * (xi**5 - 2.0 * xi**3 + 0.8 * xi)
        
        # Multi-scale harmonic interference with quantum frequency coupling
        harmonics = 0.0
        freq_mod = 1.5 + 0.5 * np.sin(0.7 * self.dim + 0.3 * np.cos(0.4 * self.dim))
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum harmonic components with dynamic scale factors
            scale_factor = 3.0**(i % 7)
            harmonics += (0.7 + 0.3 * np.sin(scale_factor * xi + 0.5 * np.cos(2 * scale_factor * xi))) * \
                        np.cos(freq_mod * scale_factor * xi + 0.4 * np.sin(3 * scale_factor * xi)) * \
                        np.exp(-0.2 * xi**2)
        
        # Cross-dimensional coupling with quantum entanglement coefficients
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Quantum-inspired asymmetric interaction with entanglement strength
                asym_strength = 1.1 + 0.2 * np.sin(0.5 * (i - j) + 0.3 * np.cos(0.2 * (i + j)))
                dist = np.sqrt((xi - xj)**2 + 0.2)
                cross += asym_strength * np.sin(22.0 * dist + 0.6 * np.cos(15.0 * dist)) * np.exp(-dist**2)
        
        # Time-varying landscape with quantum perturbations and chaotic modulation
        time_mod = 1.2 + 0.6 * np.sin(0.3 * self.dim + np.sum(x_norm) + 0.4 * np.cos(0.5 * np.sum(x_norm)))
        landscape_mod = 0.7 * np.cos(4.0 * np.sum(x_norm) + 0.5 * np.sin(6.0 * np.sum(x_norm))) + \
                       0.3 * np.sin(7.0 * np.sum(x_norm) + 0.3 * np.cos(8.0 * np.sum(x_norm)))
        
        # Combine all components with quantum-inspired dynamic weights
        weight_saddle = 0.4 + 0.2 * np.sin(self.dim * 0.4)
        weight_basins = 0.35 + 0.15 * np.cos(self.dim * 0.3)
        weight_harmonics = 0.15 + 0.2 * np.tanh(self.dim * 0.15)
        weight_cross = 0.32
        
        return time_mod * (weight_saddle * saddle + 
                          weight_basins * basins + 
                          weight_harmonics * harmonics + 
                          weight_cross * cross) + landscape_mod