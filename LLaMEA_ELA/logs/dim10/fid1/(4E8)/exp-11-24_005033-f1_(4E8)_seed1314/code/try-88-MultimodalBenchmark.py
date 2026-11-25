import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying harmonic potentials with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Chaotic harmonic base with dynamic frequency
            freq = 2.0 + 0.5 * np.sin(0.1 * i + np.sum(x[:i]) if i > 0 else 0)
            base_potential = np.sin(freq * xi) * np.cos(3 * xi) + 0.3 * np.sin(5 * xi)
            
            # Dynamic conditioning based on position and dimension
            condition = 1.0 + 0.2 * np.abs(xi) * np.cos(0.5 * i)
            
            # Asymmetric basin structure
            asymmetry = 0.1 * np.sin(xi) * np.cos(2 * xi)
            
            result += condition * base_potential + asymmetry
            
        # Cross-dimensional coupling with time-varying weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength
                coupling_strength = 0.5 * (1 + np.sin(0.2 * (i + j) + np.sum(x)))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add chaotic gradient modulation
        gradient_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic gradient component with non-monotonic behavior
            gradient_mod += np.sin(xi**3) * np.cos(4 * xi) * np.exp(-0.05 * xi**2)
            
        # Multi-scale periodicity with varying amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            amplitude = 1.0 + 0.3 * np.sin(0.3 * i)
            periodicity += amplitude * np.sin((i + 1) * xi) * np.cos(2 * (i + 1) * xi)
            
        # Combine components with adaptive weights
        result = 0.7 * result + 0.4 * cross_coupling + 0.3 * gradient_mod + 0.5 * periodicity
        
        # Add penalty for distance from origin with asymmetric scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                penalty += 0.2 * xi**4
            else:
                penalty += 0.3 * np.abs(xi)**5
                
        result += penalty
        
        return result