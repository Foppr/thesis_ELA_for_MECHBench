import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave modulation with improved resonance
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.tan(2 * x[i]) + 
                       0.1 * np.sin(13 * x[i]) * np.exp(-0.1 * np.abs(x[i])) + 
                       0.05 * np.sin(5 * x[i]) * np.cos(9 * x[i]))
        
        # Dynamic multi-peak Gaussian with time-varying skewness and improved variance
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(x[i] ** 2)
            width = 0.3 + 0.7 * (1 + np.cos(x[i])) / 2
            skew = 1.0 + 0.4 * np.sin(2 * x[i])
            gaussian += np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2)) * np.tanh(skew * x[i]) * np.cos(x[i] ** 3)
        
        # Fractal-like recursive saddle structures with enhanced complexity
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(x[i]) * np.cos(3 * x[i]) * np.exp(-np.abs(x[i])) * (1 + 0.2 * np.sin(5 * x[i]))
        
        # Cross-dimensional polynomial couplings with adaptive weights and improved interaction
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 1.0 + 0.3 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                cross_poly += weight * (x[i] ** 3 + x[j] ** 3) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Quantum harmonic oscillator-inspired component with improved potential
        quantum = 0.0
        for i in range(self.dim):
            quantum += (np.sin(2 * x[i]) * np.cos(5 * x[i])) ** 2 + 0.03 * x[i] ** 6 + 0.02 * np.sin(7 * x[i])
        
        # Adaptive fractal landscape with recursive scaling and improved smoothness
        adaptive_fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(x[i]) * np.cos(x[i] ** 2)
            adaptive_fractal += np.exp(-scale * np.abs(x[i])) * np.sin(scale * x[i] ** 2) * (1 + 0.1 * np.cos(3 * x[i]))
        
        # Multi-scale resonance peaks with complex trigonometric mixing and improved distribution
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(11 * x[i]) * np.cos(5 * x[i]) * np.log(np.abs(x[i]) + 2) * np.tan(x[i] / 3) * (1 + 0.15 * np.sin(4 * x[i]))
        
        # Gradient deception through hybrid polynomial-trigonometric mixing with improved complexity
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 4 - 2 * x[i] ** 2 + 0.5) * np.sin(x[i] ** 3) * np.cos(2 * x[i])
        
        # Complex cross-dimensional interactions with dynamic scaling factors and improved correlation
        complex_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                scale_factor = 1.0 + 0.3 * np.cos(x[i] * x[j]) * np.sin(x[i] + x[j])
                complex_cross += scale_factor * np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (x[i] ** 4 + x[j] ** 4) * np.tanh(x[i] * x[j])
        
        # Add global bias correction to reduce systematic errors
        bias_correction = 0.01 * np.sum(np.abs(x))
        
        # Combine all components with optimized weights
        return (0.17 * chaotic + 
                0.23 * gaussian + 
                0.13 * fractal + 
                0.14 * cross_poly + 
                0.09 * quantum + 
                0.08 * adaptive_fractal + 
                0.06 * resonance + 
                0.07 * deception + 
                0.06 * complex_cross + 
                bias_correction)