import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher complexity
        self.r1 = 3.95
        self.r2 = 3.85
        self.alpha = 0.7
        self.beta = 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested logistic map chaotic component with multiple iterations
        chaotic = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            # Apply nested chaotic maps for higher complexity
            for _ in range(15):
                xi = self.r1 * xi * (1 - xi)
            for _ in range(10):
                xi = self.r2 * xi * (1 - xi)
            chaotic += xi
            
        # Multi-scale harmonic interference with varying amplitudes
        harmonic = 0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            phases = [0.0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3]
            amplitudes = [1.0, 0.8, 0.6, 0.4, 0.2]
            for f, p, a in zip(freqs, phases, amplitudes):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 3.0 + p/3.0)
                
        # Dynamic conditioning based on solution proximity to global optimum
        condition = 0
        for i in range(self.dim):
            # Adaptive scaling that changes based on x[i] value
            scale_factor = 1.0 + self.alpha * np.sin(i * np.pi / self.dim) * np.exp(-0.5 * (x[i]**2))
            condition += scale_factor * (x[i]**2) * np.exp(-0.1 * abs(x[i]))
            
        # Enhanced cross-dimensional coupling with dynamic weights
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Dynamic weight based on dimension indices and solution values
                weight = np.exp(-0.2 * (i + j)) * (1.0 + 0.5 * np.sin(x[i] * x[j]))
                cross += weight * np.exp(-0.5 * (diff**2)) * np.sin(3.0 * diff)
                
        # Non-linear transformation with polynomial, exponential, and trigonometric components
        transform = 0
        for i in range(self.dim):
            # Combination of higher-order polynomial and exponential terms
            transform += (x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-0.15 * abs(x[i]))
            
        # Enhanced noise-like perturbation from chaotic system with feedback
        noise = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            for _ in range(8):
                xi = self.r1 * xi * (1 - xi)
            # Feedback mechanism that incorporates previous values
            feedback = np.sin(xi * 10.0) if i > 0 else 0.0
            noise += 0.3 * xi * np.sin(7.0 * x[i]) + 0.1 * feedback
            
        # Add global modulation based on solution quality (lower fitness values)
        modulation = 0.0
        if np.linalg.norm(x) < 2.0:
            modulation = 10.0 * np.exp(-0.5 * np.linalg.norm(x)**2)
            
        # Combine all components with adaptive weights
        result = 1.2 * chaotic + 1.0 * harmonic + 0.8 * condition + 0.6 * cross + 0.4 * transform + 0.3 * noise + modulation
        
        return result + 7.0 * self.dim  # Add offset to ensure positive fitness