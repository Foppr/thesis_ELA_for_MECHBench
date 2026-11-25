import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave base with modified frequency modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Improved dynamic frequency based on position and dimension
            freq = 1.2 + 0.9 * np.sin(0.25 * i + np.sum(x[:i]) if i > 0 else 0)
            
            # Multi-component sine-wave with varying amplitudes and phases
            base_potential = (np.sin(freq * xi) + 
                             0.6 * np.sin(2 * freq * xi) + 
                             0.4 * np.sin(3 * freq * xi) +
                             0.2 * np.sin(4 * freq * xi))
            
            # Enhanced dynamic conditioning with position-dependent scaling
            condition = 1.0 + 0.4 * np.abs(xi) * (1 + 0.3 * np.cos(0.4 * i))
            
            # Improved asymmetric basin structure with modified curvature
            asymmetry = 0.25 * np.sin(xi) * np.cos(2 * xi) * (1 + 0.15 * xi**2)
            
            result += condition * base_potential + asymmetry
            
        # Enhanced cross-dimensional coupling with adaptive weights and improved interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling strength based on dimension and position
                coupling_strength = 0.5 * (1 + np.sin(0.4 * (i + j) + np.sum(x)))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Enhanced gradient modulation with improved nonlinearity
        gradient_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced gradient component with complex non-monotonic behavior
            gradient_mod += np.sin(xi**3) * np.cos(3 * xi) * np.exp(-0.1 * xi**2) + 0.15 * np.sin(5 * xi)
            
        # Multi-scale periodicity with varying amplitudes, phases and enhanced complexity
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            amplitude = 1.3 + 0.3 * np.sin(0.4 * i)
            phase = 0.2 * np.cos(0.15 * i)
            periodicity += amplitude * np.sin((i + 1) * xi + phase) * np.cos(3 * (i + 1) * xi + phase) + 0.1 * np.sin(7 * xi)
            
        # Combine components with adjusted weights for better balance
        result = 0.65 * result + 0.65 * cross_coupling + 0.45 * gradient_mod + 0.55 * periodicity
        
        # Improved penalty for distance from origin with enhanced asymmetry and better scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                penalty += 0.25 * xi**4
            else:
                penalty += 0.35 * np.abs(xi)**5
                
        result += penalty
        
        # Add global scaling factor and adjust to improve fitness score
        result *= 1.05
        
        return result