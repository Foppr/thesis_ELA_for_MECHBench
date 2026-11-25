import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for oscillatory components
        self.omega = 2.0 * np.pi
        self.kappa = 1.5
        self.lambda_ = 0.8
        self.mu = 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component with multiple frequencies
        periodic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Multiple harmonic terms with varying amplitudes and frequencies
            freq1 = 1.0 + 0.2 * np.sin(i * 0.5)
            freq2 = 1.5 + 0.3 * np.cos(i * 0.7)
            freq3 = 2.0 + 0.1 * np.sin(i * 0.9)
            
            periodic_sum += (
                0.5 * np.sin(freq1 * xi) +
                0.3 * np.cos(freq2 * xi) +
                0.2 * np.sin(freq3 * xi)
            ) ** 2
            
        # Radial harmonic component with multiple polynomial terms
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_sum = 0
        else:
            radial_sum = (
                self.kappa * radius**2 +
                0.5 * self.lambda_ * radius**3 +
                0.1 * self.mu * radius**4 *
                (1 + 0.3 * np.sin(3 * radius) + 0.2 * np.cos(2 * radius))
            )
            
        # Cross-dimensional coupling with interaction strengths based on distance
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)  # Avoid division by zero
                # Distance-dependent coupling with exponential decay
                coupling = np.exp(-dist / (1 + 0.1 * i)) * np.sin(self.omega * dist)
                coupling_sum += coupling ** 2
                
        # Asymmetric component with different behavior in positive and negative regions
        asymmetric_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric polynomial terms that penalize deviation from zero
            if xi >= 0:
                asymmetric_sum += 0.4 * xi**3 + 0.1 * xi**4
            else:
                asymmetric_sum += 0.6 * xi**3 + 0.2 * xi**4
                
        # Dimensionality scaling and normalization
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weights
        result = scale_factor * (0.8 * periodic_sum + 0.6 * radial_sum + 0.5 * coupling_sum + asymmetric_sum)
        
        # Add small random noise for robustness
        noise = 0.003 * np.random.normal(0, 1)
        
        return result + noise + 0.2 * self.dim