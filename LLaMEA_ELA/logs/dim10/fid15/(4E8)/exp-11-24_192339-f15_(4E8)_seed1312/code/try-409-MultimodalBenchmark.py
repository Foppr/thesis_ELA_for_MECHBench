import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with quantum-like interference and dynamic phase modulation
        chaos = 0
        for i in range(self.dim):
            degree = 3 + int(np.abs(x[i]) * 0.7) % 5
            poly_term = np.sum([np.power(x[i], k) * np.sin(k * x[i] + np.cos(k * 0.5)) for k in range(1, degree + 1)])
            chaos += poly_term * np.exp(-0.15 * x[i]**2)
        
        # Modified radial basis function with quantum harmonic modulation and spectral bandwidth scaling
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            width = 0.3 + 0.4 * np.sin(0.5 * x[i] + np.pi/4)
            bandwidth = 1.0 + 0.2 * np.sin(0.3 * x[i])
            for center in centers:
                rbf += np.exp(-0.3 * ((x[i] - center) / (width * bandwidth))**2) * np.cos(0.2 * x[i])
        
        # Enhanced chaotic gradient coupling with fractal scaling and dynamic curvature modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                curvature = 1.0 + 0.3 * np.sin(0.4 * (x[i] + x[j]))
                coupling += np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.3 * (x[i] - x[j])**2 * curvature) * np.sin(0.5 * (x[i] + x[j]))
        
        # Quantum-inspired oscillatory components with multi-scale interference and dynamic frequency modulation
        oscillation = 0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.6 * x[i] + np.cos(0.3 * x[i]))
            scale = 1.2 + 0.3 * np.cos(0.7 * x[i] + np.sin(0.4 * x[i]))
            oscillation += scale * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive fractal basin structure with dynamic saddle points and phase-shifted transition functions
        basin = 0
        for i in range(self.dim):
            transition = 1.0 / (1.0 + np.exp(-3.0 * (x[i] - 2.0 + 0.5 * np.sin(0.7 * x[i]))))
            basin += transition * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
        
        # Additional chaotic ridge structures with dynamic curvature and spectral phase coupling
        ridge = 0
        for i in range(self.dim):
            ridge += np.sin(2.0 * x[i] + np.cos(0.5 * x[i])) * np.cos(1.5 * x[i] + np.sin(0.3 * x[i])) * np.exp(-0.05 * x[i]**2)
        
        # Spectral bandwidth modulation and phase interference terms
        spectral = 0
        for i in range(self.dim):
            phase = np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
            spectral += np.exp(-0.2 * x[i]**2) * np.sin(3.0 * x[i] + phase) * np.cos(2.0 * x[i] + phase)
        
        # Combine all components with optimized weights and chaotic scaling
        return 0.21 * chaos + 0.22 * rbf + 0.17 * coupling + 0.21 * oscillation + 0.11 * basin + 0.03 * ridge + 0.05 * spectral