import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based base with recursive harmonic structure
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            
            # Recursive frequency modulation with fractal scaling
            freq = 2.0 + 1.5 * np.sin(0.1 * i + np.sum(x[:i]) if i > 0 else 0)
            freq *= (1.0 + 0.3 * np.sin(0.5 * i + np.sum(x[:i]) if i > 0 else 0))
            
            # Multi-harmonic sine-wave with fractal amplitude scaling
            base_potential = (np.sin(freq * xi) + 
                             0.6 * np.sin(2 * freq * xi) + 
                             0.4 * np.sin(3 * freq * xi) +
                             0.2 * np.sin(5 * freq * xi))
            
            # Dynamic conditioning with fractal scaling factor
            condition = 1.0 + 0.5 * np.abs(xi) * (1 + 0.3 * np.cos(0.4 * i + np.sum(x[:i]) if i > 0 else 0))
            
            # Asymmetric basin structure with fractal curvature
            asymmetry = 0.3 * np.sin(xi) * np.cos(2 * xi) * (1 + 0.2 * xi**2) * np.sin(0.3 * i)
            
            result += condition * base_potential + asymmetry
            
        # Enhanced cross-dimensional coupling with fractal weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on dimension and position
                coupling_strength = 0.5 * (1 + np.sin(0.4 * (i + j) + np.sum(x)))
                coupling_strength *= (1.0 + 0.2 * np.cos(0.3 * i + 0.4 * j))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Fractal gradient modulation with multi-scale nonlinearity
        gradient_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal enhanced gradient component
            gradient_mod += np.sin(xi**3) * np.cos(3 * xi) * np.exp(-0.1 * xi**2) + \
                           0.15 * np.sin(5 * xi) + \
                           0.08 * np.sin(7 * xi) * np.cos(0.5 * xi)
            
        # Multi-scale periodicity with fractal amplitudes and phases
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            amplitude = 1.5 + 0.5 * np.sin(0.5 * i + np.sum(x[:i]) if i > 0 else 0)
            phase = 0.4 * np.cos(0.2 * i + np.sum(x[:i]) if i > 0 else 0)
            periodicity += amplitude * np.sin((i + 1) * xi + phase) * np.cos(3 * (i + 1) * xi + phase)
            
        # Combine components with fractal weights
        result = 0.8 * result + 0.7 * cross_coupling + 0.5 * gradient_mod + 0.6 * periodicity
        
        # Fractal penalty for distance from origin with multi-scale asymmetry
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi >= 0:
                penalty += 0.3 * xi**5
            else:
                penalty += 0.4 * np.abs(xi)**6
                
        result += penalty
        
        # Add fractal scaling factor and adjust to improve fitness score
        result *= 1.2
        
        return result