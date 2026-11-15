import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add fractal-like periodic components with exponentially increasing frequency
        for i in range(1, min(8, self.dim + 1)):
            freq = 3**i
            term = np.sin(freq * np.pi * x) * np.cos(freq * np.pi * x)
            result += 0.15 * np.sum(term**2)
        
        # Recursive fractal structure using a modified Barnsley-like construction with chaotic scaling
        fractal_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            scale = 0.35  # Slightly reduced scaling factor
            for depth in range(1, 7):
                # Apply transformation that creates self-similarity with chaotic perturbation
                xi = scale * (xi - 0.5) + 0.5 + 0.05 * np.sin(100 * xi)
                # Add penalty at each level with dynamic weighting
                fractal_penalty += np.sin(15 * xi) * np.exp(-depth / 3.5) * np.cos(depth * np.pi / 3.0)  # Slightly faster decay
        
        # Add chaotic component using a modified sine-Gordon-like terms with time-varying parameters
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.exp(-i / self.dim) * np.sin(5 * i)
        
        # Add multiple nested minima with exponentially decaying depths and randomized positions
        nested_penalty = 0.0
        for k in range(1, 10):
            # Create k-th level minima with randomized positions
            level_scale = 1.0 / (3**k)
            loc = np.full(self.dim, level_scale)
            # Random perturbation to create complex structure
            for i in range(self.dim):
                loc[i] = level_scale * np.sin(k * i * np.pi / self.dim) + 0.1 * np.cos(k * i)
            distance = np.sum((x - loc)**2)
            nested_penalty += np.exp(-distance / (2.0 * (k**2))) * np.sin(k * np.pi / 4.0)
        
        # Add dynamic frequency modulation to increase complexity
        mod_freq = 0.0
        for i in range(self.dim):
            mod_freq += np.sin(10 * x[i]) * np.cos(12 * x[i]) * np.exp(-i / self.dim) * (1 + 0.1 * np.sin(i))
        
        # Add spiral attractor components for increased complexity
        spiral_penalty = 0.0
        for i in range(self.dim):
            spiral_penalty += np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.exp(-i / (self.dim * 1.5)) * np.sin(i * np.pi / 4.0)  # Increased decay rate
        
        # Add memory-dependent evaluation: previous evaluation affects current
        memory_effect = 0.0
        if hasattr(self, 'last_x'):
            diff = np.sum((x - self.last_x)**2)
            memory_effect = 0.1 * np.exp(-diff / 10.0)
        self.last_x = x.copy()
        
        result += fractal_penalty + chaotic_term + 0.6 * nested_penalty + 0.2 * mod_freq + 0.4 * spiral_penalty + memory_effect  # Increased spiral weight
        
        return result