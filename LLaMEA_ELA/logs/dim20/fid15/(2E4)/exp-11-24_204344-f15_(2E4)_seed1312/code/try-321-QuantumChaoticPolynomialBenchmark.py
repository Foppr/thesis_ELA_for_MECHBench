import numpy as np

class QuantumChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired oscillation with phase modulation and amplitude scaling
        quantum_term = 0.0
        for i in range(self.dim):
            phase = np.sin(i * 0.7 + self.dim * 0.5) * np.cos(i * 0.4 + self.dim * 0.3)
            amp = 1.2 + 0.8 * np.sin(i * 0.6 + self.dim * 0.4)
            freq = 2.0 + 3.0 * np.cos(i * 0.5 + self.dim * 0.6)
            quantum_term += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase)
        
        # Adaptive radial basis function with dynamic center and width adjustments
        radial_term = 0.0
        for i in range(self.dim):
            center = -3.5 + 7.0 * np.sin(i * 0.8 + self.dim * 0.4)
            width = 0.2 + 0.9 * np.cos(i * 0.6 + self.dim * 0.5)
            radial_term += np.exp(-0.5 * ((x[i] - center) / width) ** 2) * (1.0 + 0.3 * np.sin(i * 0.9))
        
        # Asymmetric gradient field with cubic and exponential components
        grad_term = 0.0
        for i in range(self.dim):
            bias = 1.5 * np.cos(i * 1.2 + self.dim * 0.3)
            grad_term += (x[i] ** 3) * np.exp(-0.3 * x[i] ** 2) * (1.0 + bias * 0.5)
        
        # Fractal-like recursive structure with multi-scale features and self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.9 + 0.6 * np.cos(i * 1.4 + self.dim * 0.3)
            fractal_term += scale * np.sin(x[i] * scale) * np.cos(x[i] * scale * 0.7)
        
        # Dynamic coupling with non-linear interaction and adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(i * j * 0.4)
                coupling = weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                coupling_term += coupling ** 2
        
        # Multi-peak landscape with varying peak characteristics and interaction
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.0 + 1.5 * np.cos(i * 0.7)
            w1 = 0.3 + 0.6 * np.sin(i * 0.5)
            h2 = 1.8 + 1.2 * np.sin(i * 0.6)
            w2 = 0.4 + 0.5 * np.cos(i * 0.7)
            p1 = -2.0 + 4.0 * np.cos(i * 1.1)
            p2 = -3.0 + 6.0 * np.sin(i * 0.8)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.4 * peak1 + 0.6 * peak2
        
        # Chaotic perturbation with higher dimensional coupling and modified feedback
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_factor = np.cos(x[i] * 0.5 + self.dim * 0.4) * np.sin(x[i] * 0.3)
            chaos_term += chaos_factor * np.cos(x[i] ** 2 * 0.4)
        
        # Final combination with optimized weights and conditioning
        total = 0.32 * quantum_term + 0.28 * radial_term + 0.19 * grad_term + 0.14 * fractal_term + 0.03 * coupling_term + 0.06 * peak_term + 0.04 * chaos_term
        
        # Global scaling with chaotic modulation and adaptive behavior
        global_scale = 1.0 + 0.4 * np.cos(self.dim * 0.6) * np.sin(self.dim * 0.35)
        
        return total * global_scale