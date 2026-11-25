import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation component
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.tan(2 * x[i]) + 0.1 * np.sin(13 * x[i])
        
        # Dynamic multi-peak Gaussian with time-varying skewness
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(x[i] ** 2)
            width = 0.5 + 0.5 * np.cos(x[i])
            skew = 1.0 + 0.3 * np.sin(2 * x[i])
            gaussian += np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2)) * np.tanh(skew * x[i])
        
        # Fractal-like recursive saddle structures
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(x[i]) * np.cos(3 * x[i]) * np.exp(-np.abs(x[i]))
        
        # Cross-dimensional polynomial couplings with adaptive weights
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 1.0 + 0.2 * np.sin(x[i] * x[j])
                cross_poly += weight * (x[i] ** 3 + x[j] ** 3) * np.cos(x[i] - x[j])
        
        # Quantum harmonic oscillator-inspired component
        quantum = 0.0
        for i in range(self.dim):
            quantum += (np.sin(2 * x[i]) * np.cos(5 * x[i])) ** 2 + 0.05 * x[i] ** 6
        
        # Adaptive fractal landscape with recursive scaling
        adaptive_fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(x[i])
            adaptive_fractal += np.exp(-scale * np.abs(x[i])) * np.sin(scale * x[i] ** 2)
        
        # Multi-scale resonance peaks with complex trigonometric mixing
        resonance = 0.0
        for i in range(self.dim):
            resonance += np.sin(11 * x[i]) * np.cos(5 * x[i]) * np.log(np.abs(x[i]) + 3) * np.tan(x[i] / 3)
        
        # Gradient deception through hybrid polynomial-trigonometric mixing
        deception = 0.0
        for i in range(self.dim):
            deception += (x[i] ** 4 - 2 * x[i] ** 2 + 0.5) * np.sin(x[i] ** 3)
        
        # Complex cross-dimensional interactions with dynamic scaling factors
        complex_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                scale_factor = 1.0 + 0.4 * np.cos(x[i] * x[j])
                complex_cross += scale_factor * np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (x[i] ** 4 + x[j] ** 4)
        
        # Combine all components with varying weights
        return 0.18 * chaotic + 0.22 * gaussian + 0.12 * fractal + 0.15 * cross_poly + 0.08 * quantum + 0.08 * adaptive_fractal + 0.07 * resonance + 0.06 * deception + 0.06 * complex_cross