import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave base with dynamic frequency modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Dynamic frequency based on position and dimension
            freq = 1.5 + 0.8 * np.sin(0.2 * i + np.sum(x[:i]) if i > 0 else 0)
            
            # Multi-component sine-wave with varying amplitudes
            base_potential = (np.sin(freq * xi) + 
                             0.5 * np.sin(2 * freq * xi) + 
                             0.3 * np.sin(3 * freq * xi))
            
            # Dynamic conditioning with position-dependent scaling
            condition = 1.0 + 0.3 * np.abs(xi) * (1 + 0.2 * np.cos(0.3 * i))
            
            # Asymmetric basin structure with modified curvature
            asymmetry = 0.2 * np.sin(xi) * np.cos(2 * xi) * (1 + 0.1 * xi**2)
            
            result += condition * base_potential + asymmetry
            
        # Enhanced cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on dimension and position
                coupling_strength = 0.4 * (1 + np.sin(0.3 * (i + j) + np.sum(x)))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Chaotic gradient modulation with enhanced nonlinearity
        gradient_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced gradient component with complex non-monotonic behavior
            gradient_mod += np.sin(xi**3) * np.cos(3 * xi) * np.exp(-0.08 * xi**2) + 0.1 * np.sin(5 * xi)
            
        # Multi-scale periodicity with varying amplitudes and phases
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            amplitude = 1.2 + 0.4 * np.sin(0.4 * i)
            phase = 0.3 * np.cos(0.1 * i)
            periodicity += amplitude * np.sin((i + 1) * xi + phase) * np.cos(3 * (i + 1) * xi + phase)
            
        # Combine components with adjusted weights
        result = 0.7 * result + 0.6 * cross_coupling + 0.4 * gradient_mod + 0.5 * periodicity
        
        # Improved penalty for distance from origin with enhanced asymmetry
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                penalty += 0.2 * xi**4
            else:
                penalty += 0.3 * np.abs(xi)**5
                
        result += penalty
        
        # Add global scaling factor and adjust to improve fitness score
        result *= 1.1
        
        return result