import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with dynamic frequencies and amplitudes
        layer1 = np.sum(np.sin(7 * np.pi * x_norm * np.exp(-0.1 * np.abs(x_norm))) * 
                       np.cos(4 * np.pi * x_norm * np.exp(-0.05 * np.abs(x_norm))))
        
        layer2 = np.sum(np.sin(12 * np.pi * x_norm**2 * np.exp(-0.2 * x_norm**2)) * 
                       np.cos(6 * np.pi * x_norm**2 * np.exp(-0.1 * x_norm**2)))
        
        layer3 = np.sum(np.sin(15 * np.pi * x_norm**3 * np.exp(-0.3 * np.abs(x_norm**3))) * 
                       np.cos(7 * np.pi * x_norm**3 * np.exp(-0.15 * np.abs(x_norm**3))))
        
        # Adaptive polynomial basin terms with dimension-dependent coefficients
        poly_basin = np.sum((0.6 + 0.2 * np.sin(np.pi * x_norm)) * x_norm**5 + 
                           (0.4 + 0.1 * np.cos(np.pi * x_norm)) * x_norm**4 + 
                           (0.3 + 0.15 * np.sin(2 * np.pi * x_norm)) * x_norm**3)
        
        # Quantum-like cross-dimensional entanglement with complex phase interactions
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                phase = np.sin(np.pi * (x_norm[i] + x_norm[j]) / (1 + dist))
                cross_interaction += np.exp(-dist**2) * phase * np.cos(3 * np.pi * dist)
        
        # Saddle structure with fractional powers and log-periodic oscillations
        saddle = np.sum(x_norm**(3.5) * np.cos(3 * np.pi * x_norm * np.log(np.abs(x_norm) + 1)))
        
        # Fractal-like noise component with self-similar structure
        fractal_noise = 0.0
        for k in range(1, 6):
            fractal_noise += (0.1 / k) * np.sin(k * np.pi * x_norm * np.exp(-k * np.abs(x_norm)))
        
        # Add global scaling and asymmetric distortion
        result = 2.0 * (layer1 + layer2 + layer3) + 1.2 * poly_basin + 0.8 * cross_interaction + 0.6 * saddle + fractal_noise
        
        # Add bounded random perturbation
        noise = 0.02 * np.random.random() - 0.01
        
        return result + noise