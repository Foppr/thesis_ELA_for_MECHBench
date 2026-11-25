import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher complexity and fractal characteristics
        self.r1 = 3.995
        self.r2 = 3.94
        self.r3 = 3.98
        self.alpha = 0.92
        self.beta = 0.45
        self.gamma = 0.35
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested logistic map chaotic component with multiple iterations and higher chaos
        chaotic = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            # Apply nested chaotic maps for higher complexity
            for _ in range(25):
                xi = self.r1 * xi * (1 - xi)
            for _ in range(20):
                xi = self.r2 * xi * (1 - xi)
            for _ in range(10):
                xi = self.r3 * xi * (1 - xi)
            chaotic += xi
            
        # Multi-scale harmonic interference with varying amplitudes and phase shifts
        harmonic = 0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
            phases = [0.0, np.pi/8, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi]
            amplitudes = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
            for f, p, a in zip(freqs, phases, amplitudes):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 2.0 + p/2.0)
                
        # Dynamic conditioning based on solution proximity to global optimum with enhanced nonlinearity
        condition = 0
        for i in range(self.dim):
            # Adaptive scaling that changes based on x[i] value and dimension
            scale_factor = 1.0 + self.alpha * np.sin(i * np.pi / self.dim) * np.exp(-0.3 * (x[i]**2))
            condition += scale_factor * (x[i]**5) * np.exp(-0.2 * abs(x[i]))
            
        # Enhanced cross-dimensional coupling with dynamic weights and additional interaction terms
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                # Dynamic weight based on dimension indices and solution values
                weight = np.exp(-0.3 * (i + j)) * (1.0 + 0.7 * np.sin(x[i] * x[j])) * (1.0 + self.gamma * np.cos(x[i] + x[j]))
                cross += weight * np.exp(-0.3 * (diff**2)) * np.sin(5.0 * diff) + 0.2 * np.cos(2.0 * diff) + 0.1 * np.tan(0.5 * diff)
                
        # Non-linear transformation with polynomial, exponential, and trigonometric components
        transform = 0
        for i in range(self.dim):
            # Combination of higher-order polynomial and exponential terms
            transform += (x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-0.25 * abs(x[i]))
            
        # Enhanced noise-like perturbation from chaotic system with feedback and additional harmonics
        noise = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            for _ in range(15):
                xi = self.r1 * xi * (1 - xi)
            # Feedback mechanism that incorporates previous values and additional harmonic
            feedback = np.sin(xi * 15.0) if i > 0 else 0.0
            noise += 0.5 * xi * np.sin(10.0 * x[i]) + 0.2 * feedback + 0.1 * np.cos(5.0 * x[i]) + 0.08 * np.tan(0.3 * x[i])
            
        # Add global modulation based on solution quality (lower fitness values)
        modulation = 0.0
        if np.linalg.norm(x) < 2.5:
            modulation = 20.0 * np.exp(-0.4 * np.linalg.norm(x)**2)
            
        # Combine all components with adaptive weights and additional terms
        result = 1.8 * chaotic + 1.5 * harmonic + 1.3 * condition + 1.0 * cross + 0.7 * transform + 0.5 * noise + modulation
        
        return result + 12.0 * self.dim  # Add offset to ensure positive fitness