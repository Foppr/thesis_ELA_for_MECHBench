import numpy as np

class AsymmetricMomentumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize asymmetric saddle points
        self.saddle_centers = np.random.uniform(-4.0, 4.0, dim)
        self.saddle_heights = np.random.uniform(0.5, 3.0, dim)
        self.momentum_directions = np.random.uniform(-1.0, 1.0, dim)
        self.frequency_couplings = np.random.uniform(0.1, 2.0, dim)
        self.curvature_params = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Asymmetric saddle point contributions
        for i in range(self.dim):
            xi = x[i]
            center = self.saddle_centers[i]
            height = self.saddle_heights[i]
            momentum = self.momentum_directions[i]
            curvature = self.curvature_params[i]
            
            # Asymmetric quadratic saddle with directional momentum
            diff = xi - center
            asymmetric_term = height * (diff**2 - 1.0)**2 + momentum * diff**3
            
            # Add curvature modulation
            curved_term = curvature * np.sin(2.0 * xi) * np.cos(0.5 * xi)
            
            result += asymmetric_term + curved_term
            
        # Directional momentum gradient coupling
        for i in range(self.dim):
            xi = x[i]
            momentum = self.momentum_directions[i]
            
            # Momentum-based directional influence
            momentum_component = momentum * np.exp(-0.5 * xi**2) * np.sin(3.0 * xi)
            result += momentum_component
            
        # Spectral frequency coupling between dimensions
        for i in range(self.dim):
            xi = x[i]
            freq_coupling = self.frequency_couplings[i]
            
            # Frequency-dependent cross-dimension interaction
            spectral_term = 0.0
            for j in range(self.dim):
                if i != j:
                    xj = x[j]
                    spectral_term += np.sin(freq_coupling * (xi - xj)) * np.cos(0.3 * (xi + xj))
            
            result += 0.2 * spectral_term
            
        # Add global directional bias
        direction_bias = np.sum(self.momentum_directions * x)
        result += 0.5 * direction_bias**2
        
        # Add non-linear scaling with exponential modulation
        exp_mod = np.exp(0.1 * np.sum(x))
        result *= (1.0 + 0.2 * exp_mod)
        
        return result