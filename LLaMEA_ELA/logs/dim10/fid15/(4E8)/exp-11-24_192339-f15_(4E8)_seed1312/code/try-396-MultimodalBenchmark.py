import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion with quantum-like interference
        chaos = 0
        for i in range(self.dim):
            degree = 3 + int(np.abs(x[i]) * 0.7) % 5
            poly_term = np.sum([np.power(x[i], k) * np.sin(k * x[i]) for k in range(1, degree + 1)])
            chaos += poly_term * np.exp(-0.15 * x[i]**2)
        
        # Modified radial basis function with quantum harmonic modulation
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            width = 0.3 + 0.4 * np.sin(0.5 * x[i] + np.pi/4)
            for center in centers:
                rbf += np.exp(-0.3 * ((x[i] - center) / width)**2) * np.cos(0.2 * (x[i] - center))
        
        # Enhanced chaotic gradient coupling with fractal dimension modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x[i] - x[j])
                coupling += np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.3 * dist**2) * (1 + 0.1 * np.sin(dist * np.pi))
        
        # Quantum-inspired oscillatory components with dynamic phase coupling
        oscillation = 0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.6 * x[i] + np.pi/3)
            scale = 1.2 + 0.3 * np.cos(0.8 * x[i] + np.pi/6)
            phase = 0.5 * np.sin(0.4 * x[i]**2)
            oscillation += scale * np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase)
        
        # Adaptive fractal basin structure with multi-scale sigmoidal transitions
        basin = 0
        for i in range(self.dim):
            transition1 = 1.0 / (1.0 + np.exp(-3.0 * (x[i] - 2.0)))
            transition2 = 1.0 / (1.0 + np.exp(-1.5 * (x[i] + 2.0)))
            basin += (transition1 * (x[i]**5 - 3*x[i]**3 + 2*x[i]) + 
                     transition2 * (x[i]**4 - 2*x[i]**2 + 1)) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale harmonic interference with dynamic amplitude modulation
        interference = 0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(0.3 * x[i] * (self.dim + 1))
            for k in range(1, min(6, self.dim + 1)):
                interference += amp_mod * np.sin(k * x[i]) * np.cos(k * x[i]**2) * np.exp(-0.05 * k)
        
        # Combine all components with optimized weights
        return (0.22 * chaos + 0.23 * rbf + 0.18 * coupling + 
                0.22 * oscillation + 0.12 * basin + 0.03 * interference)