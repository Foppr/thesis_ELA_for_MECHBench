import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal radial component with nested minima structure
        r = np.sqrt(np.sum(x**2))
        fractal_radial = 0.5 * r**4 * (1.0 + 0.6 * np.sin(15.0 * r) * np.cos(11.0 * r) * np.sin(8.0 * r))
        
        # Chaotic wave interactions with multiple frequency components
        chaotic_waves = 0.0
        for i in range(self.dim):
            chaotic_waves += (1.2 * np.sin(8.0 * x[i] + 0.7 * np.sin(15.0 * x[i])) + 
                            0.8 * np.cos(6.0 * x[i] + 0.5 * np.cos(12.0 * x[i])) + 
                            0.4 * np.sin(3.0 * x[i] + 0.2 * np.sin(20.0 * x[i])) + 
                            0.2 * np.cos(10.0 * x[i]) * np.sin(5.0 * x[i]))
        
        # Nested fractal basin structure with varying scales
        basin_structure = 0.0
        for i in range(self.dim):
            basin_structure += (0.8 * np.sin(4.0 * x[i])**2 * np.cos(7.0 * x[i]) + 
                             0.5 * np.cos(9.0 * x[i])**2 * np.sin(6.0 * x[i]) + 
                             0.3 * np.sin(11.0 * x[i]) * np.cos(3.0 * x[i]) + 
                             0.1 * np.cos(13.0 * x[i]) * np.sin(2.0 * x[i]))
        
        # Enhanced cross-dimensional coupling with chaotic interaction patterns
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction strength based on fractal geometry
                strength = 0.6 + 0.4 * np.sin(0.7 * (i**2 + j**2)) * np.cos(0.5 * i * j) * np.sin(0.3 * (i+j))
                coupling += strength * x[i] * x[j] * np.sin(5.0 * (x[i]**2 + x[j]**2)) * np.cos(2.0 * x[i] * x[j])
        
        # Hybrid noise component with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += (0.2 * np.sin(25.0 * x[i]) * np.cos(20.0 * x[i]) + 
                     0.15 * np.cos(30.0 * x[i]) * np.sin(15.0 * x[i]) + 
                     0.1 * np.sin(35.0 * x[i]) * np.cos(10.0 * x[i]) + 
                     0.05 * np.cos(40.0 * x[i]))
        
        # Multi-modal component with irregular fitness surfaces
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (3.0 * np.sin(5.0 * x[i]) * np.cos(7.0 * x[i]) + 
                          2.5 * np.cos(10.0 * x[i])**3 + 
                          2.0 * np.sin(15.0 * x[i])**2 + 
                          1.5 * np.cos(20.0 * x[i]) * np.sin(8.0 * x[i]))
        
        # Adaptive curvature with fractal scaling properties
        curvature = 0.0
        for i in range(self.dim):
            # Fractal-based curvature variation
            curv = 1.0 + 0.7 * np.sin(0.5 * i) * np.cos(0.4 * i**2) * np.sin(0.3 * i**3)
            curvature += curv * x[i]**2 * (1.0 + 0.5 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]))
        
        # Global scaling with fractal dimension characteristics
        scale = 1.0 + 0.3 * np.sum(np.sin(x)**4) + 0.2 * np.sum(np.cos(x)**5) + 0.1 * np.sum(np.tan(x)**2)
        
        # Penalty for being far from origin to encourage convergence
        penalty = 0.12 * r**5
        
        return scale * (fractal_radial + chaotic_waves + basin_structure + coupling + noise + modal_term + curvature) + penalty