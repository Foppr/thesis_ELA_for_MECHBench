import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired sinusoidal component with phase modulation and superposition
        quantum_component = np.sum(0.3 * np.sin(3.0 * x + 0.4 * np.cos(0.5 * x) + 0.2 * np.sin(0.3 * x)) * 
                                  np.cos(2.0 * x + 0.3 * np.sin(0.4 * x) + 0.1 * np.cos(0.2 * x)) * 
                                  (1.0 + 0.15 * np.sin(0.6 * x) * np.cos(0.3 * x)))
        
        # Fractal radial basis function with self-similar center positioning and multi-scale variance
        rbf = 0.0
        for i in range(self.dim):
            center = 1.5 * np.sin(0.9 * i + 0.5 * x[i]) * np.cos(0.4 * i) - 1.2 * np.sin(0.3 * x[i])
            variance = 0.1 + 0.05 * np.sin(0.7 * i + 0.2 * np.sum(x))
            rbf += 1.5 * np.exp(-0.2 * (x[i] - center)**2 / (0.15 + variance))
        
        # Enhanced chaotic tent map with quantum coupling and fractal frequency modulation
        tent = 0.0
        for i in range(self.dim):
            if i == 0:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
            else:
                tent_val = 2.0 * np.abs(x[i]) * (x[i] < 0.5) + 2.0 * (1.0 - np.abs(x[i])) * (x[i] >= 0.5)
                # Quantum coupling with fractal frequency
                freq = 0.8 + 0.2 * np.sin(0.5 * i + 0.3 * np.sum(x[:i]))
                tent_val *= np.sin(freq * x[i-1] + 0.3 * np.cos(freq * x[i-1]) + 0.1 * np.sin(0.9 * x[i-2] if i > 1 else x[i]))
            # Fractal scaling factor
            scale_factor = 1.0 + 0.1 * np.sin(0.4 * i + 0.2 * np.sum(x[:i]))
            tent += tent_val * scale_factor
        
        # Fractal radial distance with quantum harmonic modulation and multi-scale coupling
        radial = np.sum(0.7 * np.sqrt(np.sum(x**2)) * 
                        (1.0 + 0.25 * np.sin(2.5 * np.sum(x)) + 0.15 * np.cos(0.6 * np.sum(x))) *
                        (1.0 + 0.1 * np.sin(0.4 * np.sum(x)) * np.cos(0.3 * np.sum(x))) *
                        (1.0 + 0.05 * np.sin(0.8 * np.sum(x))))
        
        # Quantum harmonic oscillations with multi-dimensional amplitude modulation
        harmonic = np.sum(0.4 * np.sin(4.0 * x + 0.3 * np.cos(0.6 * x) + 0.1 * np.sin(0.4 * x)) * 
                          np.cos(2.5 * x + 0.2 * np.sin(0.5 * x) + 0.15 * np.cos(0.3 * x)) * 
                          (1.0 + 0.2 * np.sin(0.7 * x) * np.cos(0.4 * x)) * 
                          (1.0 + 0.1 * np.cos(0.5 * x) * np.sin(0.3 * x)))
        
        # Combine all components with quantum-adaptive weights
        weight_quantum = 1.0 + 0.25 * np.sin(0.15 * np.sum(x) + 0.1 * np.cos(0.2 * np.sum(x)))
        weight_rbf = 1.0 + 0.15 * np.cos(0.25 * np.sum(x) + 0.1 * np.sin(0.3 * np.sum(x)))
        weight_tent = 1.0 + 0.2 * np.sin(0.2 * np.sum(x) + 0.15 * np.cos(0.25 * np.sum(x)))
        weight_radial = 1.0 + 0.1 * np.cos(0.3 * np.sum(x) + 0.1 * np.sin(0.2 * np.sum(x)))
        weight_harmonic = 1.0 + 0.08 * np.sin(0.35 * np.sum(x) + 0.1 * np.cos(0.25 * np.sum(x)))
        
        result = weight_quantum * quantum_component + weight_rbf * rbf + weight_tent * tent + weight_radial * radial + weight_harmonic * harmonic
        
        return result