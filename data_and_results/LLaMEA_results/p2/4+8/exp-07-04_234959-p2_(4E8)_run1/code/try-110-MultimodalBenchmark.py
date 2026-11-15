import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.global_min = np.array([2.5 * np.sin(i * 0.5 + self.t) * np.cos(i * 0.2 + self.t) for i in range(dim)])
        self.memory = np.zeros(dim)
        self.history = []
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial with self-similar structure
        f1 = np.sum(np.power(np.abs(x - self.global_min), 1.7) + 0.3 * np.power(x - self.global_min, 4.0))
        
        # Quantum interference terms with complex phase modulation
        phase = np.exp(1j * (x + self.t))
        f2 = np.sum(np.real(phase * np.exp(-0.3 * np.abs(x - self.global_min)**2)) * np.sin(5.0 * x))
        
        # Exponential barrier with logarithmic scaling
        f3 = np.sum(np.exp(-0.2 * (x - self.global_min)**2) * np.log(1.0 + np.abs(x)))
        
        # Trigonometric with fractional frequency and adaptive amplitude
        f4 = np.sum(np.sin(2.5 * x + np.cos(0.5 * x)) * np.exp(-0.15 * np.abs(x)) * (1.0 + 0.2 * np.sin(self.t)))
        
        # Memory-dependent component with chaotic feedback
        memory_effect = np.sum(self.memory * np.sin(x))
        f5 = memory_effect * np.exp(-0.1 * np.sum((x - self.global_min)**2))
        
        # Hyperbolic and inverse trigonometric interactions
        f6 = np.sum(np.arctan(x) * np.cosh(0.5 * x) * np.log(1.0 + np.abs(x)))
        
        # Time-varying global minimum with chaotic dynamics
        self.t += 0.02
        new_min = np.array([2.5 * np.sin(i * 0.5 + self.t) * np.cos(i * 0.2 + self.t) for i in range(self.dim)])
        self.memory = 0.7 * self.memory + 0.3 * (new_min - self.global_min)
        self.global_min = new_min
        
        # Add chaotic noise with memory effect
        noise = np.random.normal(0, 0.02, self.dim)
        noise = 0.5 * noise + 0.5 * np.mean(self.history[-5:]) if len(self.history) >= 5 else noise
        self.history.append(noise)
        if len(self.history) > 10:
            self.history.pop(0)
            
        f7 = np.sum((x - self.global_min + noise)**2.5 * np.cos(x))
        
        # Combine all components with dynamic weights
        weights = [0.25, 0.2, 0.15, 0.12, 0.1, 0.08, 0.05]
        components = [f1, f2, f3, f4, f5, f6, f7]
        
        result = sum(w * c for w, c in zip(weights, components))
        
        # Add a small chaotic perturbation to the final result
        chaotic_perturbation = 0.001 * np.sum(np.sin(self.t * x))
        return result + chaotic_perturbation