import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave modulation with quaternion-inspired coupling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.tan(2 * x[i]) + 
                       0.1 * np.sin(13 * x[i]) + 
                       0.05 * np.sin(5 * x[i]) * np.cos(9 * x[i])) * (1.0 + 0.2 * np.sin(x[i] ** 2))
        
        # Dynamic multi-peak Gaussian with time-varying skewness and adaptive kurtosis
        gaussian = 0.0
        for i in range(self.dim):
            center = np.sin(x[i] ** 2)
            width = 0.5 + 0.5 * np.cos(x[i])
            skew = 1.0 + 0.3 * np.sin(2 * x[i])
            kurt = 1.0 + 0.4 * np.cos(3 * x[i])
            gaussian += (np.exp(-0.5 * ((x[i] - center) ** 2) / (width ** 2)) * 
                        np.tanh(skew * x[i]) * (1.0 + 0.1 * np.sin(kurt * x[i])))
        
        # Fractal-like recursive saddle structures with dynamic scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(x[i]) * np.cos(3 * x[i]) * np.exp(-np.abs(x[i])) * (1.0 + 0.3 * np.sin(x[i] ** 2))
        
        # Cross-dimensional polynomial couplings with adaptive weights and dynamic exponents
        cross_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = 1.0 + 0.2 * np.sin(x[i] * x[j])
                exponent = 2.0 + 0.5 * np.cos(x[i] + x[j])
                cross_poly += weight * (x[i] ** exponent + x[j] ** exponent) * np.cos(x[i] - x[j])
        
        # Quantum harmonic oscillator-inspired component with phase modulation
        quantum = 0.0
        for i in range(self.dim):
            quantum += ((np.sin(2 * x[i]) * np.cos(5 * x[i])) ** 2 + 
                       0.05 * x[i] ** 6 + 
                       0.03 * np.sin(4 * x[i]) * np.cos(8 * x[i]))
        
        # Adaptive fractal landscape with recursive scaling and dynamic phase shifts
        adaptive_fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(x[i])
            phase_shift = 0.2 * np.cos(x[i] ** 2)
            adaptive_fractal += np.exp(-scale * np.abs(x[i])) * np.sin(scale * x[i] ** 2 + phase_shift)
        
        # Multi-scale resonance peaks with complex trigonometric mixing and dynamic amplitude
        resonance = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.3 * np.sin(x[i] ** 2)
            resonance += amplitude * np.sin(11 * x[i]) * np.cos(5 * x[i]) * np.log(np.abs(x[i]) + 3) * np.tan(x[i] / 3)
        
        # Gradient deception through hybrid polynomial-trigonometric mixing with dynamic coefficients
        deception = 0.0
        for i in range(self.dim):
            coef1 = 1.0 + 0.2 * np.sin(x[i])
            coef2 = 0.8 + 0.3 * np.cos(x[i])
            deception += (coef1 * x[i] ** 4 - coef2 * x[i] ** 2 + 0.5) * np.sin(x[i] ** 3)
        
        # Complex cross-dimensional interactions with dynamic scaling factors and memory effects
        complex_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                scale_factor = 1.0 + 0.4 * np.cos(x[i] * x[j])
                memory = 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                complex_cross += scale_factor * np.exp(-0.5 * ((x[i] - x[j]) ** 2)) * (x[i] ** 4 + x[j] ** 4) * memory
        
        # Novel quantum-inspired interference component
        quantum_interference = 0.0
        for i in range(self.dim):
            quantum_interference += np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.exp(-x[i] ** 2) * (1.0 + 0.2 * np.sin(x[i] ** 3))
        
        # Combined weighted components
        return (0.15 * chaotic + 
                0.20 * gaussian + 
                0.10 * fractal + 
                0.14 * cross_poly + 
                0.07 * quantum + 
                0.08 * adaptive_fractal + 
                0.06 * resonance + 
                0.05 * deception + 
                0.05 * complex_cross + 
                0.05 * quantum_interference)