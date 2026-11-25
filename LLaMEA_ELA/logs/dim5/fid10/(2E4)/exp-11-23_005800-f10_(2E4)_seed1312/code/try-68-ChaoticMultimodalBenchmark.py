import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher complexity
        self.r1 = 3.99
        self.r2 = 3.92
        self.alpha = 0.85
        self.beta = 0.4
        # Fractal noise parameters
        self.fractal_scale = 0.1
        self.fractal_freq = 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested logistic map chaotic component with multiple iterations
        chaotic = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            # Apply nested chaotic maps for higher complexity
            for _ in range(20):
                xi = self.r1 * xi * (1 - xi)
            for _ in range(15):
                xi = self.r2 * xi * (1 - xi)
            chaotic += xi
            
        # Multi-scale harmonic interference with varying amplitudes
        harmonic = 0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
            phases = [0.0, np.pi/8, np.pi/4, np.pi/2, 2*np.pi/3, 3*np.pi/4, 7*np.pi/8]
            amplitudes = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]
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
                weight = np.exp(-0.3 * (i + j)) * (1.0 + 0.7 * np.sin(x[i] * x[j]))
                cross += weight * np.exp(-0.5 * (diff**2)) * np.sin(4.0 * diff)
                
        # Non-linear transformation with polynomial, exponential, and trigonometric components
        transform = 0
        for i in range(self.dim):
            # Combination of higher-order polynomial and exponential terms
            transform += (x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-0.2 * abs(x[i]))
            
        # Enhanced noise-like perturbation from chaotic system with feedback
        noise = 0
        for i in range(self.dim):
            norm_x = (x[i] + 5.0) / 10.0
            xi = norm_x
            for _ in range(10):
                xi = self.r1 * xi * (1 - xi)
            # Feedback mechanism that incorporates previous values
            feedback = np.sin(xi * 12.0) if i > 0 else 0.0
            noise += 0.4 * xi * np.sin(9.0 * x[i]) + 0.15 * feedback
            
        # Fractal noise component for increased landscape complexity
        fractal = 0
        for i in range(self.dim):
            # Apply fractal noise based on multiple frequencies and amplitudes
            freqs = [self.fractal_freq, self.fractal_freq*2, self.fractal_freq*4]
            amps = [self.fractal_scale, self.fractal_scale*0.5, self.fractal_scale*0.25]
            for f, a in zip(freqs, amps):
                fractal += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0)
                
        # Add global modulation based on solution quality (lower fitness values)
        modulation = 0.0
        if np.linalg.norm(x) < 1.5:
            modulation = 15.0 * np.exp(-0.3 * np.linalg.norm(x)**2)
            
        # Combine all components with adaptive weights
        result = 1.5 * chaotic + 1.2 * harmonic + 1.0 * condition + 0.8 * cross + 0.6 * transform + 0.5 * noise + 0.4 * fractal + modulation
        
        return result + 10.0 * self.dim  # Add offset to ensure positive fitness